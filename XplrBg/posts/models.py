from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model
from django.db import models

from XplrBg.core.mixins.model_mixins import AuditInfoMixin
from XplrBg.locations.models import Location

UserModel = get_user_model()


class Post(AuditInfoMixin, models.Model):
    TEXT_MAX_LENGTH = 200

    text = models.TextField(
        max_length=TEXT_MAX_LENGTH,
        null=False,
        blank=False,
    )
    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,

    )
    location = models.ForeignKey(
        Location,
        on_delete=models.RESTRICT,
        null=False,
        blank=False
    )

    image = CloudinaryField(
        'image',
        null=True,
        blank=True,
    )
