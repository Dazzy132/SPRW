from behaviors.behaviors import Timestamped
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import OuterRef, Q, Subquery, Exists, Count
from django.shortcuts import get_object_or_404
from smart_selects.db_fields import ChainedForeignKey

User = get_user_model()


class ChatQuerySet(models.QuerySet):

    def get_count_new_messages(self, user_id: int):
        return self.annotate(
            new_messages=Count(
                'messages',
                filter=~Q(messages__sender_id=user_id) & Q(messages__read=False)
            )
        )


class Chat(Timestamped):
    objects = ChatQuerySet.as_manager()

    owner = models.ForeignKey(
        User,
        verbose_name="Создатель чата",
        related_name="selfDialogs",
        on_delete=models.CASCADE
    )
    opponent = models.ForeignKey(
        User,
        verbose_name="Второй участник",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Диалог {self.owner} и {self.opponent}"

    @staticmethod
    def validate_chat_exists(owner, opponent):
        if owner == opponent:
            raise ValidationError("Чат с самим с собой запрещен")

        if Chat.objects.filter(
                models.Q(owner=owner, opponent=opponent) |
                models.Q(owner=opponent, opponent=owner)
        ).exists():
            raise ValidationError(
                f"Чат с участниками {owner} и {opponent} уже существует"
            )

    @staticmethod
    def find_chat(user1, user2):
        return get_object_or_404(
            Chat,
            models.Q(owner=user1, opponent=user2) |
            models.Q(owner=user2, opponent=user1)
        )

    def clean(self):
        self.validate_chat_exists(self.owner, self.opponent)

    # TODO: Для ограничения в shell (но возможно будет вызываться 2 clean)
    # def save(self, *args, **kwargs):
    #     self.full_clean()
    #     super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'


class Message(Timestamped):
    chat = models.ForeignKey(
        Chat,
        verbose_name="Диалог",
        related_name="messages",
        on_delete=models.CASCADE
    )
    sender = models.ForeignKey(
        User,
        verbose_name="Автор",
        related_name="messages",
        on_delete=models.CASCADE
    )
    replied = ChainedForeignKey(
        'self',
        verbose_name='Ответ на',
        blank=True,
        null=True,
        chained_field="chat",
        chained_model_field="chat",

    )
    text = models.TextField(verbose_name="Message text")
    read = models.BooleanField(verbose_name="Read", default=False)

    def __str__(self):
        return f"{self.sender.username} отправил {self.text[:20]}"
