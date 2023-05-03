from dataclasses import dataclass   

from django.db.models import CASCADE, CharField, ForeignKey

from complaints.models.complaints import Complaints


class CommentComplaint(Complaints):
    @dataclass
    class CAUSE_OF_COMPLAINT:
        DRUGS = 'drugs'
        CHILD_PORNOGRAPHY = 'child pornography'
        VIOLENCE = 'violence'
        SUSPICIOUS_ACTIVITY = 'suspicious activity'
    CAUSE_OF_COMPLAINT_CHOISE = (
        (CAUSE_OF_COMPLAINT.DRUGS,
         'Комментарий содержит пропаганду наркотиков'),
        (CAUSE_OF_COMPLAINT.CHILD_PORNOGRAPHY,
         'Комментарий содержит детскую порнографию'),
        (CAUSE_OF_COMPLAINT.VIOLENCE,
         'Комментарий содержит призывы к насилию'),
        (CAUSE_OF_COMPLAINT.SUSPICIOUS_ACTIVITY,
         'Комментарий оставлен пользователем с подозрительной активностью')
    )
    complaint = CharField(
        'Жалоба',
        choices=CAUSE_OF_COMPLAINT_CHOISE,
        max_length=200)
    comment = ForeignKey(
        'posts.Comment',
        on_delete=CASCADE,
        verbose_name='комментарий на который поступила жалоба')

    class Meta:
        verbose_name = 'Жалоба на комментарий'
        verbose_name_plural = 'Жалобы на комментарии'

    def __str__(self):
        return f"Жалоба на комментарий: {self.comment}"
