from django.db import models

from django.contrib.auth import get_user_model


class Profile(models.Model):
    user = models.OneToOneField(
        get_user_model(),
        on_delete=models.CASCADE,
        primary_key=True)
    photo = models.ImageField(
        null=True,
        blank=True,
        verbose_name='Фото пользователя')
    profile_status = models.CharField(
        max_length=150,
        blank=True,
        null=True,
        verbose_name='статус пользователя')
    is_private = models.BooleanField(
        default=False,
        verbose_name='Закрыт ли профиль пользователя')

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return self.user.username
