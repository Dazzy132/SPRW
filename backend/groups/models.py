from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Groups(models.Model):
    name = models.CharField(
        max_length=45,
        verbose_name='Название группы')
    group_slug = models.SlugField(
        verbose_name='Название группы в поиске', unique=True)
    title = models.TextField(
        verbose_name='Описание группы',
        blank=True, null=True)
    image = models.ImageField(
        upload_to='groups/images',
        verbose_name='Фото группы',
        blank=True, null=True)
    is_closed_group = models.BooleanField(
        verbose_name='Закрыта ли группа',
        default=False)
    group_creator = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name='Создатель группы',
        related_name='group_creator')
    group_moderator = models.ManyToManyField(
        User,
        verbose_name='Модерация группы',
        related_name='group_moderator',
        blank=True)
                            
    subscribers = models.ManyToManyField(
        User, verbose_name='подписчики',
        related_name='subscribers',
        blank=True)

    class Meta:
        verbose_name = 'Пользовательская руппа'
        verbose_name_plural = 'Пользовательские группы'

    def __str__(self):
        return self.name

