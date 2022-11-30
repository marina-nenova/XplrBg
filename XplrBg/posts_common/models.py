from django.contrib.auth import get_user_model
from django.db import models

from XplrBg.core.mixins.model_mixins import AuditInfoMixin
from XplrBg.posts.models import Post

UserModel = get_user_model()


class PostLike(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )


class PostComment(AuditInfoMixin, models.Model):
    MAX_TEXT_LENGTH = 300

    text = models.CharField(
        max_length=MAX_TEXT_LENGTH,
        null=False,
        blank=False,
    )

    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        null=False,
        blank=True,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )
