from django.core.exceptions import ValidationError


class NoSpacesPasswordValidator:
    """Проверка на отсутствие пробелов в пароле"""

    def validate(self, password, user=None):
        if ' ' in password:
            raise ValidationError(
                'Пароль не может содержать пробелы',
                code='password_no_spaces'
            )

    def get_help_text(self):
        return 'Пароль не должен содержать пробелы'