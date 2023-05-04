from dataclasses import dataclass   

from django.db.models import CASCADE, CharField, ForeignKey

from complaints.models.complaints import Complaints


class ProfileComplaint(Complaints):
    @dataclass
    class CAUSE_OF_COMPLAINT:
        CLONE = 'clone'
        CHILD_PORNOGRAPHY = 'child pornography'
        SPAM = 'spam'
    CAUSE_OF_COMPLAINT_CHOISE = (
        (CAUSE_OF_COMPLAINT.CLONE,
         'Пользователь копирует ваши фото и информацию '
         'и пытается выдать себя за вас'),
        (CAUSE_OF_COMPLAINT.CHILD_PORNOGRAPHY,
         'В профиле содержится детская порнография'),
        (CAUSE_OF_COMPLAINT.SPAM,
         'Пользователь рассылает рекламные сообщения, комментарии '
         'или другим способом распространяет рекламу '
         'в не предназначенных для этого местах.')
    )

    complaint = CharField(
        'Жалоба',
        choices=CAUSE_OF_COMPLAINT_CHOISE,
        max_length=200)
    profile = ForeignKey(
        'users.Profile',
        on_delete=CASCADE,
        verbose_name='Профиль на который поступила жалоба')

    class Meta:
        verbose_name = 'Жалоба на профиль'
        verbose_name_plural = 'Жалобы на профиль'

    def __str__(self):
        return f"Жалоба на пост: {self.profle}"
