from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.api.serializers import UserListSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    @action(
        detail=False, methods=["GET"], permission_classes={IsAuthenticated}
    )
    def me(self, request):
        return Response(self.serializer_class(request.user).data)