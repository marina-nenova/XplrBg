from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from .tasks import remove_post_image_on_post_delete
from XplrBg.posts.models import Post
import cloudinary.uploader


@receiver(pre_save, sender=Post)
def deleting_old_image_on_post_edit(sender, instance, **kwargs):
    if sender.objects.filter(pk=instance.pk).exists():
        if instance.pk:
            old_image = Post.objects.get(pk=instance.pk).image
            new_image = instance.image
            if old_image and old_image.url != new_image.url:
                cloudinary.uploader.destroy(old_image.public_id)


@receiver(post_delete, sender=Post)
def deleting_post_image_on_delete_post(sender, instance, **kwargs):
    if instance.image:
        remove_post_image_on_post_delete.delay(instance.image.public_id)
