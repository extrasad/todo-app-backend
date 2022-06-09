from rest_framework import serializers

from core.todos.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)
    class Meta:
        model = Todo
        exclude = []
        
        extra_kwargs = {
            "user": {"required": False},
        }

