from django.contrib.auth import get_user_model
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from chats.api.serializers import ChatSerializer, MessageSerializer
from chats.models import Chat, Message
from django.db.models import Q

User = get_user_model()


class ChatViewSet(ModelViewSet):
    serializer_class = ChatSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        try:
            user = get_object_or_404(User, id=kwargs.get('pk'))

            if self.request.user == user:
                return Response(
                    {'error': 'Чат с собой запрещен'},
                    status=status.HTTP_403_FORBIDDEN
                )

            chat = get_object_or_404(
                Chat,
                Q(owner=self.request.user, opponent=user) |
                Q(owner=user, opponent=self.request.user)
            )
            serializer = self.get_serializer(chat)
            return Response(serializer.data)
        except Http404:
            return Response(
                {'error': 'Вы еще не начали диалог с этим пользователем'},
                status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        return (
            Chat.objects.filter(
                Q(owner=self.request.user) | Q(opponent=self.request.user)
            )
            .select_related("owner", "opponent")
        )


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer

    def get_chat(self):
        to_user = get_object_or_404(
            User, pk=self.kwargs.get('user_id')
        )
        return get_object_or_404(
            Chat,
            Q(owner=self.request.user, opponent=to_user) |
            Q(owner=to_user, opponent=self.request.user)
        )

    def get_queryset(self):
        return Message.objects.filter(chat=self.get_chat())

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user, chat=self.get_chat())
