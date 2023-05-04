from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsRequestUserOrReadOlyProfile(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            obj.user.username == request.user.username
            or request.method in SAFE_METHODS)


class IsRequestUserOrReadOlyFriends(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            obj.user_profile == request.user.profile
            or request.method in SAFE_METHODS)
