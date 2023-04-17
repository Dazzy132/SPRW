from django.contrib.auth import get_user_model
from rest_framework import serializers

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


class PublicProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Profile
        fields = ['user_id', 'user', 'photo', 'profile_status', 'is_private']


class PrivateProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Profile
        fields = ['user']


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
