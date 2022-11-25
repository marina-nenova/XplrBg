from django.contrib import admin

from XplrBg.locations.models import LocationImage, Location, LocationCategory, LocationRegion


class LocationImageInline(admin.TabularInline):
    model = LocationImage


@admin.register(Location)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('name', 'times_visited', 'category', 'region')
    inlines = (LocationImageInline,)


@admin.register(LocationCategory)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('category_name',)


@admin.register(LocationRegion)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('region',)
