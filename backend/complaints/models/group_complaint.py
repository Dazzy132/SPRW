from django.db.models import CASCADE, ForeignKey

from complaints.models.complaints import Complaints


class GroupComplaint(Complaints):
    group = ForeignKey(
        'groups.Groups',
        on_delete=CASCADE,
        verbose_name='Группа на которую поступила жалоба')

    class Meta:
        verbose_name = 'Жалоба на группу'
        verbose_name_plural = 'Жалобы на группы'

    def __str__(self):
        return f"Жалоба на группу: {self.group}"
