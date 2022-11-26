from django.urls import path

from XplrBg.locations.views import ShowAllLocations, LocationDetails, rate_location

urlpatterns = (
    path('details-list/', ShowAllLocations.as_view(), name='all locations'),
    path('location-details/<slug:slug>/', LocationDetails.as_view(), name='location details'),
    path('rate/<int:rating>/<int:loc_pk>/', rate_location, name='rate location'),
)

from XplrBg.locations.signals import *
