from rest_framework import mixins, viewsets, status, response

from core.todos.models import Todo
from .permissions import TodoPermission
from .serializers import TodoSerializer


class TodoViewSet(
    mixins.UpdateModelMixin, 
    mixins.CreateModelMixin,
    mixins.ListModelMixin, 
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,  
    viewsets.GenericViewSet
    ):
    """
    Todo endpoints
    """

    queryset = Todo.objects.all() #noqa
    serializer_class = TodoSerializer
    permission_classes = (TodoPermission,)
    
    def get_queryset(self):
        #Filtering against user
        if self.request.user.is_superuser is False:
            user = self.request.user
            queryset = self.queryset.filter(
                user=user,
            )
            return queryset
        else:
            return self.queryset
    
    def create(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data,)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user.pk)
        return response.Response(serializer.data, status=status.HTTP_201_CREATED,)
