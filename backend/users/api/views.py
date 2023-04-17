from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet

from users.api.mixins import ListRetrieveUpdateDestroyViewSet
from users.api.permissions import IsRequestUserOrReadOly
from users.api.serializers import (FriendSerializer,
                                   PublicProfileSerializer,
                                   PrivateProfileSerializer,
                                   UserListSerializer)
from users.models.friends import Friends
from users.models.profile import Profile


User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    @action(
        detail=False, methods=["GET"], permission_classes={IsAuthenticated}
    )
    def me(self, request):
        return Response(self.serializer_class(request.user).data)


class ProfileViewSet(ListRetrieveUpdateDestroyViewSet):
    permission_classes = [IsRequestUserOrReadOly]
    queryset = Profile.objects.all()
    lookup_field = 'user__username'

    def get_serializer_class(self):
        if self.request.user.profile.is_private:
            return PrivateProfileSerializer
        return PublicProfileSerializer

    @action(detail=True, methods=['POST'])
    def add_to_friends(self, request, user__username):
        friend_request_receiver = get_object_or_404(
            Profile,
            user__username=user__username)
        if friend_request_receiver == request.user.profile:
            return Response({'error': 'Вы не можете добавить себя в друзья'})
        if Friends.objects.filter(
                application_status=Friends.APPLICSTION_STATUS.PENDING,
                user_profile=friend_request_receiver,
                friend_request_sender=request.user.profile).exists():
            return Response(
                {'error':
                 ('Вы уже отправили пользователю '
                  f'{friend_request_receiver} заявку на добавление в друзья')})
        if Friends.objects.filter(
                application_status=Friends.APPLICSTION_STATUS.PENDING,
                user_profile=request.user.profile,
                friend_request_sender=friend_request_receiver).exists():
            return Response({'error':
                             (f'{friend_request_receiver} уже отправил вам '
                              'заявку на добавление в друзья')})
        Friends.objects.create(
            user_profile=friend_request_receiver,
            friend_request_sender=request.user.profile
        )
        return Response({'success':
                         ('Заявка на добавление в друзья отправлена '
                          f'пользователю {friend_request_receiver}')})


class FriendViewSet(ListRetrieveUpdateDestroyViewSet):
    permission_classes = [IsRequestUserOrReadOly]
    serializer_class = FriendSerializer
    model = Friends
    lookup_field = 'user_profile__user__username'

    def get_queryset(self):
        if self.action in ['approve_request',
                           'decline_request',
                           'incoming_requests']:
            return self.model.objects.filter(
                user_profile=self.request.user.profile,
                application_status=self.model.APPLICSTION_STATUS.PENDING)

        elif self.action == 'out_requests':
            return self.model.objects.filter(
                friend_request_sender=self.request.user.profile,
                application_status=self.model.APPLICSTION_STATUS.PENDING)
        return self.model.objects.filter(
            user_profile=self.request.user.profile,
            application_status=self.model.APPLICSTION_STATUS.APPROVED)

    @action(detail=False, methods=['GET'])
    def incoming_requests(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def out_requests(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def approve_request(self, request,
                        user_profile__user__username=None):
        friend = self.get_object()
        friend.application_status = self.model.APPLICSTION_STATUS.APPROVED
        friend.save()
        return Response({'success':
                         f'Пользователь {friend} добавлен в друзья'})

    @action(detail=True, methods=['DELETE'])
    def decline_request(self, request,
                        user_profile__user__username=None):
        friend = self.get_object()
        friend.delete()
        return Response({'success': f'Заявка пользователя {friend} удалена'})
