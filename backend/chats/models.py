from django.contrib.auth import get_user_model
from django.db import models
from behaviors.behaviors import Timestamped

User = get_user_model()


class Chat(Timestamped):
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
        User, verbose_name="Автор",
        related_name="messages",
        on_delete=models.CASCADE
    )
    text = models.TextField(verbose_name="Message text")
    read = models.BooleanField(verbose_name="Read", default=False)

    def __str__(self):
        return f"{self.sender.username} отправил {self.text[:20]}"

