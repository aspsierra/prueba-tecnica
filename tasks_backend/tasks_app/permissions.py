from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Allows just read access to regular users
    and full access to admins
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True 
        return request.user # and request.user.is_staff 