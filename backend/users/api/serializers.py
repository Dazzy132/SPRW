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

    def to_representation(self, instance):
        if instance.is_private:
            return {'user': instance.user.username,
                    'is_private': instance.is_private}
        return super(ProfileSerializer, self).to_representation(instance)


class AddToFriendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('user_profile', 'friend_request_sender')

    def create(self, validated_data):
        user = self.context['request'].user.profile
        friend_request_receiver = validated_data['user_profile'].user.username
        if validated_data['user_profile'] == user:
            raise serializers.ValidationError(
                {'error': 'Вы не можете добавить себя в друзья'})
        if self.Meta.model.objects.filter(
                application_status=Friends.APPLICATION_STATUS.PENDING,
                user_profile=validated_data['user_profile'],
                friend_request_sender=user).exists():
            raise serializers.ValidationError(
                {'error': 'Заявка на добавление в друзья пользователя '
                          f'{friend_request_receiver} уже отправлена'})
        if self.Meta.model.objects.filter(
                user_profile=user,
                application_status=Friends.APPLICATION_STATUS.PENDING,
                friend_request_sender=validated_data['user_profile']).exists():
            raise serializers.ValidationError(
                {'error': f'Пользователь {friend_request_receiver} '
                          'уже добавил вам заявку в друзья'})
        return self.Meta.model.objects.create(
            user_profile=validated_data['user_profile'],
            friend_request_sender=user)


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

