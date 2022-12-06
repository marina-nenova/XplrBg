import cloudinary.uploader
from celery import shared_task

@shared_task
def remove_profile_photo_on_delete(old_profile_image):
    cloudinary.uploader.destroy(old_profile_image)

