from dataclasses import dataclass

from django.db import models


class Friends(models.Model):
    @dataclass
    class APPLICSTION_STATUS:
        APPROVED = 'approved'
        PENDING = 'pending'
        DECLINE = 'decline'
    APPLICSTION_STATUS_CHOISE = (
        (APPLICSTION_STATUS.APPROVED, 'заявка принята'),
        (APPLICSTION_STATUS.PENDING, 'заявка в ожидании'),
        (APPLICSTION_STATUS.DECLINE, 'заявка отклонена')
    )

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
    application_status = models.CharField(
        max_length=20,
        choices=APPLICSTION_STATUS_CHOISE,
        default='заявка в ожидании')
    
    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    def __str__(self):
        return (f'{self.user_profile.user.username} -'
                f'{self.friend_profile.user.username}')
    
    def save(self, *args, **kwargs):
        if self.application_status == 'approved':
            super().save(*args, **kwargs)
            Friends.objects.get_or_create(
                user_profile=self.friend_profile,
                friend_profile=self.user_profile,
                application_status='approved'
            )

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        Friends.objects.filter(
            user_profile=self.friend_profile,
            friend_profile=self.user_profile
        ).delete()

    @staticmethod
    def get_incoming_requests(profile):
        return Friends.objects.filter(friend_profile=profile, status='pending')