from django.contrib.auth import get_user_model
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

    def validate(self, attrs):
        if self.context.get('request').user == attrs.get("opponent"):
            raise serializers.ValidationError(
                "Вы не можете начать чат с самим собой"
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


