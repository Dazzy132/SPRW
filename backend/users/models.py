import jwt

from datetime import datetime, timedelta
from django.conf import settings
from django.db import models
from django.utils.datetime_safe import datetime
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator

from .validators import validate_username


# https://habr.com/ru/post/538040/
class User(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [
        'email',
        'first_name',
        'last_name'
    ]

    username = models.CharField(
        _("username"),
        db_index=True,
        max_length=30,
        unique=True,
        help_text='HELP TEXT',
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

    # @property
    # def token(self):
    #     """
    #     Позволяет получить токен пользователя путем вызова user.token, вместо
    #     user._generate_jwt_token(). Декоратор @property выше делает это
    #     возможным. token называется "динамическим свойством".
    #     """
    #     return self._generate_jwt_token()
    #
    # def _generate_jwt_token(self):
    #     """
    #     Генерирует веб-токен JSON, в котором хранится идентификатор этого
    #     пользователя, срок действия токена составляет 3 дня от создания
    #     """
    #     dt = datetime.now() + timedelta(days=3)
    #
    #     token = jwt.encode({
    #         'id': self.pk,
    #         'exp': dt.strftime('%Y-%m-%d %H:%M:%S')
    #     }, settings.SECRET_KEY, algorithm='HS256')
    #
    #     return token.decode('utf-8')