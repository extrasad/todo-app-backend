from rest_framework import serializers

from core.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,)
    
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name", "email", "password", "is_superuser"]
        write_only_fields = ("password",)
        
    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        #Just for testing.
        if validated_data['email'] == 'admin@test.com':
            user.is_superuser = True
        user.set_password(validated_data['password'])
        user.save()

        return user

class SendEmailSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    message = serializers.CharField(required=True)