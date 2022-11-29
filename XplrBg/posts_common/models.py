from django.contrib.auth import get_user_model
from django.db import models

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
        on_delete=models.RESTRICT,
    )
