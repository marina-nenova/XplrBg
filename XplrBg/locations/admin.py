from django.contrib import admin

from XplrBg.locations.forms import LocationImageForm, CreateLocationForm
from XplrBg.locations.models import LocationImage, Location, LocationCategory, LocationRegion


class LocationImageInline(admin.TabularInline):
    model = LocationImage
    form = LocationImageForm


@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'region')
    inlines = (LocationImageInline,)
    form = CreateLocationForm


@admin.register(LocationCategory)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


@admin.register(LocationRegion)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('region',)
