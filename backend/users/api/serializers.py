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


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field="username",
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Profile
        fields = ['user_id', 'user', 'photo', 'profile_status', 'is_private']


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ['id', 'user_profile', 'friend_profile', 'application_status']
