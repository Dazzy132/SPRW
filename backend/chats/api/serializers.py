from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers

from chats.models import Chat, Message

User = get_user_model()


class ChatSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        slug_field="username",
        default=serializers.CurrentUserDefault(),
        read_only=True
    )
    opponent = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
    )
    new_messages = serializers.IntegerField(read_only=True)

    def validate(self, attrs):
        self.Meta.model.validate_chat_exists(
            owner=self.context.get("user"),
            opponent=attrs.get("opponent")
        )

        return attrs

    class Meta:
        model = Chat
        fields = "__all__"
        read_only_fields = ["modified"]


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(
        slug_field="username", default=serializers.CurrentUserDefault(),
        read_only=True
    )
    # replied = serializers.StringRelatedField()

    class Meta:
        model = Message
        fields = "__all__"
        read_only_fields = ["modified", "read", "chat"]


