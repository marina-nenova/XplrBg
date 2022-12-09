from django.contrib import admin

from XplrBg.common.models import VisitedLocations, Wishlist


@admin.register(VisitedLocations)
class VisitedLocationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'location',)
    list_filter = ('user', 'location')
    search_fields = ('location__name', 'user__email',)
    sortable_by = ('id', 'location')


@admin.register(Wishlist)
class WishlistLocationsAdmin(admin.ModelAdmin):
    list_display = ('user', 'location',)
    list_filter = ('user', 'location')
    search_fields = ('location__name', 'user__email',)
    sortable_by = ('id', 'location')

