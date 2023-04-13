from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from users.api.serializers import ProfileSerializer, UserListSerializer
from users.api.permissions import IsUserProfileOrAdminOrReadOly
from users.models.profile import Profile
from users.models.friends import Friends
User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    @action(
        detail=False, methods=["GET"], permission_classes={IsAuthenticated}
    )
    def me(self, request):
        return Response(self.serializer_class(request.user).data)
    

class ProfileViewSet(ModelViewSet):
    permission_classes = [IsUserProfileOrAdminOrReadOly]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    lookup_field = 'user__username'

    @action(detail=True, methods=['POST'])
    def add_to_friends(self, request, username=None):
        friend_profile = get_object_or_404(Profile, user__username=username)
        Friends.objects.create(
            user_profile=request.user.profile,
            friend_profile=friend_profile
        )
        return Response({'success': True})
