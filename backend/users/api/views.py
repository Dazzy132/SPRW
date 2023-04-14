from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from users.api.serializers import ProfileSerializer, UserListSerializer, FriendSerializer
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
    def add_to_friends(self, request, user__username):
        friend_profile = get_object_or_404(Profile, user__username=user__username)
        Friends.objects.create(
            user_profile=request.user.profile,
            friend_profile=friend_profile
        )
        return Response({'success': True})

    @action(detail=True, methods=['DELETE'])
    def delete_from_friends(self, request, user__username):
        friend_profile = get_object_or_404(Profile, user__username=user__username)
        Friends.objects.filter(user_profile=request.user.profile,
            friend_profile=friend_profile).delete()
        return Response({'success': True})
    

class FriendViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FriendSerializer
    queryset = Friends.objects.all()


    @action(detail=False, methods=['GET'])
    def incoming_requests(self, request):
        profile = self.request.user.profile
        friends = Friends.get_incoming_requests(profile)
        serializer = self.get_serializer(friends, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def approve_request(self, request, pk=None):
        friend = self.get_object()
        friend.application_status = 'approved'
        friend.save()
        return Response({'success': True})