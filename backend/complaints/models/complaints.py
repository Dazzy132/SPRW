from dataclasses import dataclass

from django.contrib.auth import get_user_model
from django.db import models


class Complaints(models.Model):

    @dataclass
    class CAUSE_OF_COMPLAINT:
        DRUGS = 'drugs'
        CHILD_PORNOGRAPHY = 'child pornography'

    @dataclass
    class COMPLAINT_STATUS:
        DONE = 'done'
        IN_PROCESS = 'in_process'
        NOT_SUBSTANTIATED = 'not substantiated'

    COMPLAINT_STATUS_CHOISE = (
        (COMPLAINT_STATUS.IN_PROCESS, 'Жалоба на рассмотрении'),
        (COMPLAINT_STATUS.DONE, 'Жалоба рассмотрена'),
        (COMPLAINT_STATUS.NOT_SUBSTANTIATED, 'Жалоба не обоснована'))

    CAUSE_OF_COMPLAINT_CHOISE = (
        (CAUSE_OF_COMPLAINT.DRUGS,
         'Публикация содержит пропоганду наркотиков'),
        (CAUSE_OF_COMPLAINT.CHILD_PORNOGRAPHY,
         'Публикация содержит детскую порнография'))

    complaint = models.CharField(
        'Жалоба',
        choices=CAUSE_OF_COMPLAINT_CHOISE,
        max_length=200)

    complaint_status = models.CharField(
        'Статус жалобы',
        choices=COMPLAINT_STATUS_CHOISE,
        max_length=200, default='Жалоба на рассмотрении')

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        verbose_name='пользователь оставивший жалобу')

    class Meta:
        abstract = True
