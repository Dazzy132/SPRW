from behaviors.behaviors import Authored, Timestamped
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from smart_selects.db_fields import ChainedForeignKey

from posts.models.fields import LikesRelated


class Comment(Authored, Timestamped, LikesRelated):
    author = models.ForeignKey(get_user_model() ,on_delete=models.CASCADE)
    post = models.ForeignKey(
        'posts.Post',
        on_delete=models.CASCADE,
        verbose_name='Пост',
    )
    parent = ChainedForeignKey(
        'self', on_delete=models.DO_NOTHING, null=True,
        blank=True, related_name='replies',
        chained_field="post",
        chained_model_field="post",)
    text = models.TextField(
        "Текст",
        null=True,
        blank=True,
    )
    image = models.ImageField(
        "Изображение",
        upload_to="comments/",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.author.username} - {self.pk} - {self.text}"

    def clean(self):
        """Проверка на уровне валидации"""
        super().clean()
        if not self.text and not self.image:
            raise ValidationError(
                "Комментарий должен содержать либо текст либо картинку"
            )

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'