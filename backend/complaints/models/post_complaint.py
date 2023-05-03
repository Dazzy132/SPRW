from dataclasses import dataclass

from django.db.models import CASCADE, CharField, ForeignKey

from complaints.models.complaints import Complaints


class PostComplaint(Complaints):
    @dataclass
    class CAUSE_OF_COMPLAINT:
        DRUGS = 'drugs'
        CHILD_PORNOGRAPHY = 'child pornography'
        SPAM = 'spam'
    CAUSE_OF_COMPLAINT_CHOISE = (
        (CAUSE_OF_COMPLAINT.DRUGS,
         'Пост содержит пропаганду наркотиков'),
        (CAUSE_OF_COMPLAINT.CHILD_PORNOGRAPHY,
         'В посте содержится детская порнография'),
        (CAUSE_OF_COMPLAINT.SPAM,
         'Пост содержит рекламу, расположенную в не предназначенном месте')
    )

    complaint = CharField(
        'Жалоба',
        choices=CAUSE_OF_COMPLAINT_CHOISE,
        max_length=200)
    post = ForeignKey(
        'posts.Post',
        on_delete=CASCADE,
        verbose_name='пост на который поступила жалоба')

    class Meta:
        verbose_name = 'Жалоба на пост'
        verbose_name_plural = 'Жалобы на пост'

    def __str__(self):
        return f"Жалоба на пост: {self.post}"
