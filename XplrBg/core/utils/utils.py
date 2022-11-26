from django.db.models import Q

from XplrBg.locations.models import Location


def is_owner(request, obj):
    return request.user.pk == obj.user.pk


def filter_locations(request):
    locations = Location.objects.all().prefetch_related('location_images')
    query = request.GET.get('q', None)
    categories = request.GET.getlist('categories') or None
    regions = request.GET.getlist('regions') or None
    if query:
        locations = locations.filter(
            Q(category__category_name__icontains=query) |
            Q(region__region__icontains=query) |
            Q(name__icontains=query)
        )
    if categories:
        locations = locations.filter(category__category_name__in=categories)
    if regions:
        locations = locations.filter(region__region__in=regions)

    get_location_feature_image(locations)
    return locations

def get_location_feature_image(locations):
    for location in locations:
        location.feature_image = location.location_images.get(is_feature=True)
    return locations
