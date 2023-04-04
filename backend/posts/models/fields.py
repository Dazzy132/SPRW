from django.db import models


class LikesRelated(models.Model):
    likes = models.PositiveIntegerField(
        "Количество лайков",
        default=0
    )

    class Meta:
        abstract = True


class ViewsRelated(models.Model):
    views = models.PositiveIntegerField(
        "Количество просмотров",
        default=0
    )

    class Meta:
        abstract = True

