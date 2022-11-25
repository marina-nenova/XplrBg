from django.contrib.auth import get_user_model
from django.db import models

from XplrBg.locations.models import Location

UserModel = get_user_model()


class VisitedLocations(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    locations = models.ForeignKey(Location, on_delete=models.CASCADE)


class Wishlist(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    locations = models.ForeignKey(Location, on_delete=models.CASCADE)
