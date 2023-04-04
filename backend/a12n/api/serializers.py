from dj_rest_auth.registration.serializers import RegisterSerializer
from django.db import transaction
from rest_framework import serializers


class CustomRegisterSerializer(RegisterSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.last_name = self.data.get('last_name')
        user.first_name = self.data.get('first_name')
        user.save()
        return user

