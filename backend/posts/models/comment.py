from django.core.exceptions import ValidationError
from django.db import models
from behaviors.behaviors import Authored, Timestamped
from posts.models.fields import LikesRelated


class Comment(Authored, Timestamped, LikesRelated):
    post = models.ForeignKey(
        'posts.post',
        on_delete=models.CASCADE,
        verbose_name='Пост'
    )
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
    parent = models.ForeignKey(
        'self',
        verbose_name='Родитель',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.author.username} - {self.pk}"

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