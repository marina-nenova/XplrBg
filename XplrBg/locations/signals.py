from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
import cloudinary.uploader
from XplrBg.locations.models import LocationImage, Location


@receiver(pre_save, sender=LocationImage)
def deleting_old_location_image_on_update(sender, instance, **kwargs):
    if sender.objects.filter(pk=instance.pk).exists():
        if instance.pk:
            old_location_image = LocationImage.objects.get(pk=instance.pk).image
            new_location_image = instance.image
            if old_location_image and old_location_image != new_location_image:
                cloudinary.uploader.destroy(old_location_image.public_id)


@receiver(pre_delete, sender=Location)
def deleting_location_images_on_delete_location(sender, instance, **kwargs):
    if instance.location_images.all():
        for image in instance.location_images.all():
            cloudinary.uploader.destroy(image.image.public_id)
