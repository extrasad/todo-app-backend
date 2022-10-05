from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.conf import settings

from core.users.models import User
from .permissions import UserPermission, IsSuperAdmin
from .serializers import UserSerializer, SendEmailSerializer
from ..tasks import send_email


class UserViewSet(
    mixins.UpdateModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """
    Update user profile
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserPermission]

    def get_queryset(self):
        # Filterin Just for admin
        if self.request.user.is_superuser is False:
            queryset = self.queryset.none()
            return queryset
        else:
            return self.queryset

    @action(
        detail=False,
        methods=["post"],
        permission_classes=[IsSuperAdmin],
        url_path="send-email",
    )
    # Todo: Add graphql interface to handle send email action.
    def send_email(self, request, pk=None):
        serializer = SendEmailSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.data
            data.update({"subject": "Message from admin", "apiKey": settings.API_KEY})
            send_email.apply_async([data], countdown=5)
            return Response(status=status.HTTP_200_OK, data={"message": "email sent"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

