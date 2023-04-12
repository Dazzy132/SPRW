from behaviors.behaviors import Authored, Timestamped
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import QuerySet
from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models.fields import (Created, LikesRelated, UserRelated,
                                 ViewsRelated)


class PostQuerySet(QuerySet):
    """Дополнительные методы для objects"""

    def most_views(self) -> QuerySet["Post"]:
        """Сортировка постов по самым просматриваемым"""
        return self.order_by("-views")

    def most_likes(self) -> QuerySet["Post"]:
        """Сортировка постов по самым оцененным"""
        return self.order_by("-likes")

    def add_user_annotations(self, user_id: int) -> QuerySet["Post"]:
        return self.annotate(
            is_liked=models.Exists(
                PostLike.objects.filter(
                    user_id=user_id, post_id=models.OuterRef('pk')
                )
            )
        )


class Post(Authored, Timestamped, LikesRelated, ViewsRelated):
    objects = PostQuerySet.as_manager()

    text = models.TextField(
        "Текст поста",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/images/%Y/%m/',
        help_text="Загрузить изображение к посту",
        blank=True,
        null=True,
    )
    uuid = models.CharField(
        "Идентификатор",
        max_length=50,
        db_index=True,
        unique=True,
        null=True,
        blank=True,
    )
    tags = models.ManyToManyField(
        "posts.Tag",
        verbose_name="Теги",
        related_name="posts",
        blank=True,
    )

    def __str__(self):
        return f"{self.uuid}"

    def clean(self):
        """Проверка на уровне валидации"""
        super().clean()
        if not self.text and not self.image:
            raise ValidationError(
                "Пост должен содержать либо текст либо картинку"
            )

    class Meta:
        ordering = ['-created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


@receiver(post_save, sender=Post)
def set_post_uuid(sender, instance, **kwargs):
    """Установить значение uuid для объекта после его создания"""
    if not instance.uuid:
        instance.uuid = f"{instance.author.pk}_{(instance.author.pk << 32) + instance.pk}"
        instance.save()


class PostLike(UserRelated, Created):
    post = models.ForeignKey(
        Post,
        verbose_name="Пост",
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f"{self.user.username} лайкнул пост {self.post.pk}"

    class Meta:
        verbose_name = "Лайк к посту"
        verbose_name_plural = "Лайки к постам"
        ordering = ["-created"]
        db_table = "post_likes"
        constraints = [
            models.UniqueConstraint(
                fields=["post", "user"],
                name="unique_post_user_likes",
            )
        ]

