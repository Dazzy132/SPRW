from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator

from .validators import validate_username


class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email', 'first_name', 'last_name'
    ]

    username = models.CharField(
        _("username"),
        db_index=True,
        max_length=30,
        unique=True,
        help_text='help',
        validators=[
            MinLengthValidator(3),
            validate_username
        ]
    )
    email = models.EmailField(
        _("email"),
        db_index=True,
        max_length=40,
        unique=True,
    )
    first_name = models.CharField(
        _('first name'),
        max_length=100,
        validators=[
            RegexValidator(
                r"^[а-яА-Яa-zA-Z]+$",
                message="Имя может содержать только буквы",
            )
        ],
    )
    last_name = models.CharField(
        _('last name'), max_length=150,
        validators=[
            RegexValidator(
                r"^[а-яА-Яa-zA-Z]+$",
                message="Фамилия может содержать только буквы",
            )
        ],
    )
    updated_at = models.DateTimeField(
        _("Обновлён"),
        auto_now=True
    )

    def __str__(self):
        return self.email