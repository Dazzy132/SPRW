from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers


User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    gender = serializers.ChoiceField(
        choices=User.GENDER_CHOICES,
        required=True
    )
    # TODO: Сделать номер телефона

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.last_name = self.data.get('last_name')
        user.first_name = self.data.get('first_name')
        user.gender = self.data.get('gender')
        user.save()
        return user

