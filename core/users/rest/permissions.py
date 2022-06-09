from rest_framework import permissions


class UserPermission:
    """
    User permission to update user profile
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in ("PUT", "PATCH", "GET", "DELETE"):
            return True
        
        elif request.method in ("POST"):
            return True

        return False

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the instance
        return obj == request.user or request.user.is_superuser
    
class IsSuperAdmin:
    """
    Admin permission
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        return False

    def has_object_permission(self, request, view, obj):
        # Write permissions are only allowed to the owner of the instance
        return request.user.is_superuser
