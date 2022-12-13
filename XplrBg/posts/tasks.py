import cloudinary.uploader
from celery import shared_task


@shared_task
def remove_post_image_on_post_delete(image):
    cloudinary.uploader.destroy(image)