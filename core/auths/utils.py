from core.users.rest.serializers import UserSerializer
from core.users.models import User

def get_me_info(data, email):
    try:
        user = User.objects.get(email=email)
        serializer = UserSerializer(
            user,
        )
        data.update({"user_info": serializer.data})
        return data
    except User.DoesNotExist:
        return data

    