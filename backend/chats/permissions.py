from rest_framework.permissions import BasePermission, SAFE_METHODS


class MessageAuthorOrReadOnly(BasePermission):
    """
    Разрешение, которое позволяет пользователю только просматривать сообщения,
    но дает возможность изменять или удалять сообщения, если пользователь
    является автором.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.sender == request.user
