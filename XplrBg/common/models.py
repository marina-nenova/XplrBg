from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class VisitedLocations(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    location = models.ForeignKey("locations.Location", on_delete=models.CASCADE)


class Wishlist(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    location = models.ForeignKey("locations.Location", on_delete=models.CASCADE)
