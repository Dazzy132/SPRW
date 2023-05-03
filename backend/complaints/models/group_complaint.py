from dataclasses import dataclass   

from django.db.models import CASCADE, CharField, ForeignKey

from complaints.models.complaints import Complaints


class GroupComplaint(Complaints):
    @dataclass
    class CAUSE_OF_COMPLAINT:
        CHANGE_OF_SUBJECT = 'change of subject'
        CHILD_PORNOGRAPHY = 'child pornography'
        SPAM = 'spam'
        COMMUNITY_HACKED = 'community hacked'
    CAUSE_OF_COMPLAINT_CHOISE = (
        (CAUSE_OF_COMPLAINT.CHANGE_OF_SUBJECT,
         'Изменилось название сообщества, '
         'начали появляться материалы на другую тему'),
        (CAUSE_OF_COMPLAINT.CHILD_PORNOGRAPHY,
         'В контенте сообщества распространяется детская порнография'),
        (CAUSE_OF_COMPLAINT.SPAM,
         'Сообщество содержит много рекламы или размещает ссылки '
         'на вредоносные, или подозрительные ресурсы'),
        (CAUSE_OF_COMPLAINT.COMMUNITY_HACKED,
         'В сообществе появляются странные материалы, '
         'от руководителей приходят необычные сообщения')
    )
    complaint = CharField(
        'Жалоба',
        choices=CAUSE_OF_COMPLAINT_CHOISE,
        max_length=200)
    group = ForeignKey(
        'groups.Groups',
        on_delete=CASCADE,
        verbose_name='Группа на которую поступила жалоба')

    class Meta:
        verbose_name = 'Жалоба на группу'
        verbose_name_plural = 'Жалобы на группы'

    def __str__(self):
        return f"Жалоба на группу: {self.group}"


