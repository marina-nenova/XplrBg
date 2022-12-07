from cloudinary.models import CloudinaryField
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import MinValueValidator, MinLengthValidator
from django.db import models

from XplrBg.accounts.managers import AppUserManager
from XplrBg.core.mixins.model_mixins import AuditInfoMixin


class AppUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    USERNAME_FIELD = 'email'

    objects = AppUserManager()

    @property
    def username(self):
        return self.user_profile.get_full_name


class UserProfile(AuditInfoMixin, models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2

    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    LIVES_AT_MAX_LENGTH = 50
    LIVES_AT_MIN_LENGTH = 2

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(MinLengthValidator(FIRST_NAME_MIN_LENGTH),)
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(MinLengthValidator(LAST_NAME_MIN_LENGTH),)
    )
    lives_at = models.CharField(
        max_length=LIVES_AT_MAX_LENGTH,
        null=True,
        blank=True,
        validators=(MinLengthValidator(LIVES_AT_MIN_LENGTH),)

    )
    profile_image = CloudinaryField(
        'image',
        null=True,
        blank=True,
    )

    user = models.OneToOneField(
        AppUser,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        primary_key=True,
        related_name='user_profile'
    )

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
