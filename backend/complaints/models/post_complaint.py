from django.db.models import CASCADE, ForeignKey

from complaints.models.complaints import Complaints


class PostComplaint(Complaints):
    post = ForeignKey(
        'posts.Post',
        on_delete=CASCADE,
        verbose_name='пост на который поступила жалоба')

    class Meta:
        verbose_name = 'Жалоба на пост'
        verbose_name_plural = 'Жалобы на пост'

    def __str__(self):
        return f"Жалоба на пост: {self.post}"