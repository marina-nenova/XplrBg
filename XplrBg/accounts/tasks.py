import cloudinary.uploader
from celery import shared_task
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


@shared_task
def remove_profile_photo_on_profile_delete(old_profile_image):
    cloudinary.uploader.destroy(old_profile_image)


UserModel = get_user_model()


@shared_task
def send_email_on_register(email):
    email_content = render_to_string('email_templates/successful_sign_up.html')

    send_mail(
        subject='Welcome to Explore BG!',
        message=strip_tags(email_content),
        html_message=email_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=(email,),
    )
