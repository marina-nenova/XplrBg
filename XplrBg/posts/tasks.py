import cloudinary.uploader
from celery import shared_task


@shared_task
def remove_image_on_delete(image):
    cloudinary.uploader.destroy(image)