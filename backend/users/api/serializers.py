from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.db import IntegrityError
from users.models.profile import Profile
from users.models.friends import Friends
User = get_user_model()


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "id",
            "uuid",
            "gender",
            "group",
            "username",
            "email",
            "first_name",
            "last_name"
        ]


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
    )

    class Meta:
        model = Profile
        fields = ['user', 'photo', 'profile_status', 'is_private']

    def is_friend_request_already_sent(self, friend_request_receiver,
                                       request_user):
        return Friends.objects.filter(
            application_status=Friends.APPLICATION_STATUS.PENDING,
            user_profile=request_user.profile,
            friend_request_sender=friend_request_receiver
        ).exists()

    def add_friend_request(self, friend_request_receiver, request_user):
        try:
            Friends.objects.create(
                user_profile=friend_request_receiver,
                friend_request_sender=request_user.profile
            )
            return True
        except IntegrityError:
            return False

    def to_representation(self, instance):
        if instance.is_private:
            return {'user': instance.user.username,
                    'is_private': instance.is_private}
        return super(ProfileSerializer, self).to_representation(instance)


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ['id', 'user_profile', 'friend_request_sender',
                  'application_status']

    def update(self, instance, validated_data):
        if 'application_status' not in validated_data:
            raise serializers.ValidationError({'application_status':
                                               'Это поле обязательно'})
        instance.save(update_fields=['application_status'])
        return instance

