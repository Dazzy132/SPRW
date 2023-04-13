from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsUserProfileOrAdminOrReadOly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            obj.user.username == request.user.username or request.user.is_staff)
