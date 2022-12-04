from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import generic as views

from XplrBg.core.utils.locations_ustils import get_location_feature_image
from XplrBg.locations.models import LocationCategory, LocationRegion, Location, Rating


class ShowAllLocations(LoginRequiredMixin, views.ListView):
    context_object_name = 'all_locations'
    template_name = 'locations/locations-list.html'
    model = Location

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowAllLocations, self).get_context_data(**kwargs)

        context['visited_locations'] = Location.objects.filter(visitedlocations__user=self.request.user)
        context['wishlist_locations'] = Location.objects.filter(wishlist__user=self.request.user)
        context['location_categories'] = LocationCategory.objects.all()
        context['location_regions'] = LocationRegion.objects.all()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.__get_query()
        categories = self.__get_categories()
        regions = self.__get_regions()

        if query:
            queryset = queryset.filter(
                Q(category__category_name__icontains=query) |
                Q(region__region__icontains=query) |
                Q(name__icontains=query)
            )

        if categories:
            queryset = queryset.filter(category__category_name__in=categories)
        if regions:
            queryset = queryset.filter(region__region__in=regions)

        queryset = [get_location_feature_image(location) for location in queryset]
        return queryset

    def __get_query(self):
        query = self.request.GET.get('query', None)
        return query

    def __get_categories(self):
        category = self.request.GET.getlist('categories') or None
        return category

    def __get_regions(self):
        region = self.request.GET.getlist('regions') or None
        return region


class LocationDetails(LoginRequiredMixin, views.DetailView):
    pass
    model = Location
    template_name = 'locations/location-details.html'
    context_object_name = 'location'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LocationDetails, self).get_context_data(**kwargs)

        context['visited_locations'] = Location.objects.filter(visitedlocations__user=self.request.user)
        context['wishlist_locations'] = Location.objects.filter(wishlist__user=self.request.user)

        return context


def rate_location(request, rating: int, location):
    Rating.objects.filter(location=location, user=request.user).delete()
    location.rating_set.create(user=request.user, rating=rating)
