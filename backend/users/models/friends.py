from django.db import models


class Friends(models.Model):
    user_profile = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='friends',
        verbose_name='Профиль пользователя')
    friend_profile = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='friend_of',
        verbose_name='Друг профиля')

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    def __str__(self):
        return (f'{self.user_profile.user.username} -'
                f'{self.friend_profile.user.username}')
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        Friends.objects.get_or_create(
            user_profile=self.friend_profile,
            friend_profile=self.user_profile
        )

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        Friends.objects.filter(
            user_profile=self.friend_profile,
            friend_profile=self.user_profile
        ).delete()