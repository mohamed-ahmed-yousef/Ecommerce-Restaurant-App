from rest_framework import  permissions
class CustomStaffPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:  # Allows read-only methods (GET, HEAD, OPTIONS)
            return True

        # For other methods (POST, PUT, DELETE), check if the user is an admin
        return request.user and request.user.is_staff