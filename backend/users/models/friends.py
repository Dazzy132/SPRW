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
        (APPLICSTION_STATUS.DECLINE, 'заявка отклонена'),
    )

    user_profile = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='friends',
        verbose_name='Профиль пользователя')
    friend_request_sender = models.ForeignKey(
        'users.Profile',
        on_delete=models.CASCADE,
        related_name='friend_of',
        verbose_name='Пользователь отправивший заявку на добавление в друзья')
    application_status = models.CharField(
        max_length=20,
        choices=APPLICSTION_STATUS_CHOISE,
        default=APPLICSTION_STATUS.PENDING)

    class Meta:
        verbose_name = 'Друг'
        verbose_name_plural = 'Друзья'

    def __str__(self):
        return (f'{self.friend_request_sender.user.username}')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.application_status == self.APPLICSTION_STATUS.APPROVED:
            Friends.objects.get_or_create(
                user_profile=self.friend_request_sender,
                friend_request_sender=self.user_profile,
                application_status=self.APPLICSTION_STATUS.APPROVED
            )
        if self.application_status == self.APPLICSTION_STATUS.DECLINE:
            super().delete(*args, **kwargs)
            Friends.objects.filter(
                user_profile=self.friend_request_sender,
                friend_request_sender=self.user_profile
            ).delete()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        Friends.objects.filter(
            user_profile=self.friend_request_sender,
            friend_request_sender=self.user_profile
        ).delete()
