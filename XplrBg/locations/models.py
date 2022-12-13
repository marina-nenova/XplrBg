from cloudinary.models import CloudinaryField
from django.contrib.auth import get_user_model

from django.db import models
from django.db.models import Avg
from django.utils.text import slugify

from XplrBg.common.models import VisitedLocations
from XplrBg.core.mixins.model_mixins import AuditInfoMixin

UserModel = get_user_model()


class LocationRegion(models.Model):
    REGION_MAX_LENGTH = 20

    region = models.CharField(
        max_length=REGION_MAX_LENGTH,
    )

    def __str__(self):
        return self.region


class LocationCategory(models.Model):
    CATEGORY_MAX_LENGTH = 20

    category_name = models.CharField(
        max_length=CATEGORY_MAX_LENGTH,
    )

    def __str__(self):
        return self.category_name


class Location(AuditInfoMixin, models.Model):
    NAME_MAX_LENGTH = 30

    category = models.ForeignKey(
        LocationCategory,
        on_delete=models.SET_NULL,
        null=True,
    )
    region = models.ForeignKey(
        LocationRegion,
        on_delete=models.SET_NULL,
        null=True
    )
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False,
    )
    short_description = models.TextField(
        max_length=500,
        null=False,
        blank=False,
    )
    details = models.TextField(
        max_length=2500,
        null=False,
        blank=False,
    )
    town = models.CharField(
        max_length=25,
        null=True,
        blank=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    @property
    def average_rating(self):
        return Rating.objects.filter(location=self).aggregate(Avg("rating"))["rating__avg"] or 0

    @property
    def times_visited(self):
        return VisitedLocations.objects.filter(location=self).count()

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')
        return super().save(*args, **kwargs)


class LocationImage(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location_images")
    image = CloudinaryField(
        'image',
        null=False,
        blank=False,
    )

    is_feature = models.BooleanField(
        default=False,
    )


class Rating(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.location.name}: {self.rating}"
