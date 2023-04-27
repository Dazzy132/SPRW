from django.db.models import CASCADE, ForeignKey

from complaints.models.complaints import Complaints


class CommentComplaint(Complaints):
    comment = ForeignKey(
        'posts.Comment',
        on_delete=CASCADE,
        verbose_name='комментарий на который поступила жалоба')

    class Meta:
        verbose_name = 'Жалоба на комментарий'
        verbose_name_plural = 'Жалобы на комментарии'

    def __str__(self):
        return f"Жалоба на комментарий: {self.comment}"
