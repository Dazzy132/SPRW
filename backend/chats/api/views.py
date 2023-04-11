from django.contrib.auth import get_user_model
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from chats.api.serializers import ChatSerializer, MessageSerializer
from chats.models import Chat, Message

User = get_user_model()


class ChatViewSet(ModelViewSet):
    serializer_class = ChatSerializer

    def get_queryset(self):
        return (
            Chat.objects.filter(
                Q(owner=self.request.user) | Q(opponent=self.request.user)
            ).select_related("owner", "opponent")
        )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def check_forbidden_chat(self, user):
        if self.request.user == user:
            return Response(
                {'error': 'Чат с собой запрещен'},
                status=status.HTTP_403_FORBIDDEN
            )

    def retrieve(self, request, *args, **kwargs):
        try:
            user = get_object_or_404(User, id=kwargs.get('pk'))
            self.check_forbidden_chat(user)

            chat = Chat.find_chat(user1=self.request.user, user2=user)
            serializer = self.get_serializer(chat)
            return Response(serializer.data)

        except Http404:
            return Response(
                {'error': 'Вы еще не начали диалог с этим пользователем'},
                status=status.HTTP_404_NOT_FOUND)


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer

    def get_chat(self):
        to_user = get_object_or_404(
            User, pk=self.kwargs.get('user_id')
        )
        return Chat.find_chat(user1=self.request.user, user2=to_user)

    def get_queryset(self):
        return Message.objects.filter(chat=self.get_chat())

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, chat=self.get_chat())
