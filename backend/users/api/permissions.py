from rest_framework.permissions import BasePermission


class IsRequestUserOrReadOly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and (
            obj.user.id == request.user.id)
