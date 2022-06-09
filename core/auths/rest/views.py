
from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from ..utils import get_me_info

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        serializer = TokenObtainPairSerializer(
            data=request.data, context={"request": request}
        )

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        data = get_me_info(serializer.validated_data, request.data['email'])
        return Response(data, status=status.HTTP_200_OK)
