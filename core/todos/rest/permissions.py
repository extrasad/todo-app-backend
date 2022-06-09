from rest_framework import permissions


class TodoPermission:
    """
    Todo permissions
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the instance
        obj = obj.user
        return obj == request.user or request.user.is_superuser
