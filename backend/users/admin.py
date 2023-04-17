from django.contrib import admin
from django.contrib.auth import get_user_model

from users.models.profile import Profile
from users.models.friends import Friends
User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'first_name', 'last_name']
    search_fields = ['username', 'email']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'photo', 'is_private', 'profile_status']


@admin.register(Friends)
class FriendsAdmin(admin.ModelAdmin):
    list_display = ['user_profile', 'friend_request_sender']
