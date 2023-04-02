from modeltranslation.translator import TranslationOptions, register
from django.contrib.auth import get_user_model

User = get_user_model()


# @register(User)
# class CategoryTranslationOptions(TranslationOptions):
#     fields = ('username',)


# ru en
# python manage.py makemessages -l <locale>