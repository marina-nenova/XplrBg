from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.views import generic as views

from XplrBg.core.utils.utils import get_location_feature_image
from XplrBg.locations.models import LocationCategory, LocationRegion, Location, Rating


class ShowAllLocations(LoginRequiredMixin, views.ListView):
    context_object_name = 'all_locations'
    template_name = 'locations/locations-list.html'
    model = Location

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowAllLocations, self).get_context_data(**kwargs)

        context['visited_locations'] = self.object_list.filter(visitedlocations__user=self.request.user)
        context['wishlist_locations'] = self.object_list.filter(wishlist__user=self.request.user)
        context['location_categories'] = LocationCategory.objects.all()
        context['location_regions'] = LocationRegion.objects.all()

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.__get_query()
        if query:
            queryset = queryset.filter(
                Q(category__category_name__icontains=query) |
                Q(region__region__icontains=query) |
                Q(name__icontains=query)
            )
        get_location_feature_image(queryset)
        return queryset

    def __get_query(self):
        query = self.request.GET.get('query', None)
        return query


class LocationDetails(LoginRequiredMixin, views.DetailView):
    pass
    model = Location
    template_name = 'locations/location-details.html'
    context_object_name = 'location'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        rating = Rating.objects.filter(location=self.object, user=self.request.user.id).first()
        self.object.user_rating = rating.rating if rating else 0
        return context


def rate_location(request, rating: int, location):
    Rating.objects.filter(location=location, user=request.user).delete()
    location.rating_set.create(user=request.user, rating=rating)
