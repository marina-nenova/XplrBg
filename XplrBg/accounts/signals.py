import cloudinary.uploader
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import UserProfile
from .tasks import remove_profile_photo_on_delete
UserModel = get_user_model()


@receiver(pre_save, sender=UserProfile)
def deleting_old_profile_pic_on_update(sender, instance, **kwargs):
    if instance.profile_image:
        old_profile_image = UserProfile.objects.get(pk=instance.pk).profile_image
        new_profile_image = instance.profile_image
        if old_profile_image and old_profile_image.url != new_profile_image.url:
            cloudinary.uploader.destroy(old_profile_image.public_id)


@receiver(post_delete, sender=UserProfile)
def deleting_profile_pic_on_delete_profile(sender, instance, **kwargs):
    if instance.profile_image:
        remove_profile_photo_on_delete.delay(instance.profile_image.public_id)


@receiver(post_delete, sender=UserProfile)
def deleting_user_on_delete_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()
