from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from users.models.profile import Profile
from users.models.users import User
from users.models.friends import Friends


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Friends)
def approve_friend_request(sender, instance, **kwargs):
    if instance.application_status == instance.APPLICATION_STATUS.APPROVED:
        Friends.objects.get_or_create(
            user_profile=instance.friend_request_sender,
            friend_request_sender=instance.user_profile,
            application_status=instance.APPLICATION_STATUS.APPROVED)


@receiver(post_delete, sender=Friends)
def delete_friends(sender, instance, **kwargs):
    Friends.objects.filter(
        user_profile=instance.friend_request_sender,
        friend_request_sender=instance.user_profile
    ).delete()
