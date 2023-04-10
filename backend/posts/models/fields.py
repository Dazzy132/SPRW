from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class LikesRelated(models.Model):
    likes = models.PositiveIntegerField(
        "Количество лайков",
        default=0
    )

    class Meta:
        abstract = True


class ViewsRelated(models.Model):
    views = models.PositiveIntegerField(
        "Количество просмотров",
        default=0
    )

    class Meta:
        abstract = True


class UserRelated(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="%(app_label)s_%(class)s_user"
    )

    class Meta:
        abstract = True


class Created(models.Model):
    created = models.DateTimeField(
        "Дата",
        auto_now_add=True
    )