from behaviors.behaviors import Slugged
from django.db import models


class Tag(Slugged):
    name = models.CharField(
        "Название",
        max_length=50,
        unique=True,
        null=False,
        blank=False,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
