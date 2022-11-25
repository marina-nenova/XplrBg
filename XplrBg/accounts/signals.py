import cloudinary.uploader
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import UserProfile

UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=UserModel)
def save_user_profile(sender, instance, **kwargs):
    instance.user_profile.save()


@receiver(pre_save, sender=UserProfile)
def deleting_old_profile_pic_on_update(sender, instance, **kwargs):
    if sender.objects.filter(pk=instance.pk).exists():
        if instance.pk:
            old_profile_image = UserProfile.objects.get(pk=instance.pk).profile_image
            new_profile_image = instance.profile_image
            if old_profile_image and old_profile_image.url != new_profile_image.url:
                cloudinary.uploader.destroy(old_profile_image.public_id)