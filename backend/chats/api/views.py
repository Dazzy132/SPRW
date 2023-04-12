from django.contrib.auth import get_user_model
from django.db.models import Q, OuterRef
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from chats.api.serializers import ChatSerializer, MessageSerializer
from chats.models import Chat, Message
from chats.permissions import MessageAuthorOrReadOnly

User = get_user_model()


class ChatViewSet(ModelViewSet):
    serializer_class = ChatSerializer

    def get_queryset(self):
        user = self.request.user

        return (
            Chat.objects.filter(
                Q(owner=user) | Q(opponent=user)
            ).select_related("owner", "opponent")
            .prefetch_related("messages")
            .get_count_new_messages(user)
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['user'] = self.request.user
        return context

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @staticmethod
    def check_forbidden_chat(user1, user2):
        if user1 == user2:
            return Response(
                {'error': 'Чат с собой запрещен'},
                status=status.HTTP_403_FORBIDDEN
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            current_user = self.request.user
            user = get_object_or_404(User, id=kwargs.get('pk'))
            self.check_forbidden_chat(current_user, user)

            chat = Chat.objects.filter(
                Q(owner=current_user, opponent=user) |
                Q(owner=user, opponent=current_user)
            ).get_count_new_messages(current_user)

            chat[0].messages.filter(sender=user).update(read=True)

            serializer = self.get_serializer(chat[0])
            return Response(serializer.data)

        except (Http404, IndexError):
            return Response(
                {'error': 'Вы еще не начали диалог с этим пользователем'},
                status=status.HTTP_404_NOT_FOUND
            )


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    permission_classes = [MessageAuthorOrReadOnly]

    def get_chat(self):
        to_user = get_object_or_404(
            User, pk=self.kwargs.get('user_id')
        )
        return Chat.find_chat(user1=self.request.user, user2=to_user)

    def get_queryset(self):
        return (
            Message.objects.filter(chat=self.get_chat())
            .select_related("sender")
        )

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, chat=self.get_chat())
