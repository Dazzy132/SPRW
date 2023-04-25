from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status
from users.api.mixins import ListRetrieveUpdateDestroyViewSet
from users.api.permissions import (IsRequestUserOrReadOlyFriends,
                                   IsRequestUserOrReadOlyProfile)
from users.api.serializers import (FriendSerializer,
                                   ProfileSerializer,
                                   UserListSerializer)
from users.models.friends import Friends
from users.models.profile import Profile


User = get_user_model()


class UserViewSet(ReadOnlyModelViewSet):
    serializer_class = UserListSerializer
    queryset = User.objects.all()

    @action(detail=False, methods=["GET"],
            permission_classes={IsAuthenticated})
    def me(self, request):
        return Response(self.serializer_class(request.user).data)


class ProfileViewSet(ListRetrieveUpdateDestroyViewSet):
    permission_classes = [IsRequestUserOrReadOlyProfile]
    serializer_class = ProfileSerializer
    queryset = Profile.objects.select_related('user')
    lookup_field = 'user__username'

    @action(detail=True, methods=['POST'])
    def add_to_friends(self, request, user__username):
        friend_request_receiver = get_object_or_404(
            Profile, user__username=user__username)
        if friend_request_receiver == request.user.profile:
            return Response({'error': 'Вы не можете добавить себя в друзья'},
                            status=status.HTTP_400_BAD_REQUEST)
        if self.get_serializer().is_friend_request_already_sent(
                friend_request_receiver, request.user):
            return Response({'error':
                             (f'{friend_request_receiver} уже отправил '
                              'вам заявку на добавление в друзья')},
                            status=status.HTTP_400_BAD_REQUEST)
        if self.get_serializer().add_friend_request(friend_request_receiver,
                                                    request.user):
            return Response({'success':
                             ('Заявка на добавление в друзья отправлена '
                              f'пользователю {friend_request_receiver}')},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'error':
                             ('Вы уже отправили заявку пользователю '
                              f'{friend_request_receiver}')},
                            status=status.HTTP_400_BAD_REQUEST)


class FriendViewSet(ListRetrieveUpdateDestroyViewSet):
    permission_classes = [IsRequestUserOrReadOlyFriends]
    serializer_class = FriendSerializer
    model = Friends
    lookup_field = 'friend_request_sender__user__username'

    def get_queryset(self):
        if self.action in ['approve_request',
                           'decline_request',
                           'incoming_requests']:
            return self.model.objects.filter(
                user_profile=self.request.user.profile,
                application_status=self.model.APPLICATION_STATUS.PENDING)

        elif self.action == 'out_requests':
            return self.model.objects.filter(
                friend_request_sender=self.request.user.profile,
                application_status=self.model.APPLICATION_STATUS.PENDING)
        return self.model.objects.filter(
            user_profile=self.request.user.profile,
            application_status=self.model.APPLICATION_STATUS.APPROVED)

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
                        friend_request_sender__user__username=None):
        friend = self.get_object()
        friend.application_status = self.model.APPLICATION_STATUS.APPROVED
        friend.save()
        return Response({'success':
                         f'Пользователь {friend} добавлен в друзья'})

    @action(detail=True, methods=['DELETE'])
    def decline_request(self, request,
                        friend_request_sender__user__username=None):
        friend = self.get_object()
        friend.delete()
        return Response({'success': f'Заявка пользователя {friend} удалена'})
