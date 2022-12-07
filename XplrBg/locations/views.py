from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views

from XplrBg.core.mixins.views_mixins import FilteredLocationsView
from XplrBg.locations.filters import LocationsFilter
from XplrBg.locations.models import Location, Rating


class ShowAllLocations(LoginRequiredMixin, FilteredLocationsView):
    context_object_name = 'all_locations'
    template_name = 'locations/locations-list.html'
    model = Location
    filterset_class = LocationsFilter
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowAllLocations, self).get_context_data(**kwargs)

        context['visited_locations'] = Location.objects.filter(visitedlocations__user=self.request.user)
        context['wishlist_locations'] = Location.objects.filter(wishlist__user=self.request.user)

        return context


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


class TopTenLocationsView(views.ListView):
    template_name = 'locations/top-ten-locations.html'
    model = Location
    context_object_name = 'top_ten_rated'
    paginate_by = 10
    ordering = 'name'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopTenLocationsView, self).get_context_data(**kwargs)

        context['top_ten_visited'] = sorted(Location.objects.all(), key=lambda a: -a.times_visited)[:10]
        return context

    def get_queryset(self):
        queryset = super(TopTenLocationsView, self).get_queryset()
        queryset = sorted(Location.objects.all(), key=lambda a: -a.average_rating)[:10]
        return queryset


def rate_location(request, rating: int, location):
    Rating.objects.filter(location=location, user=request.user).delete()
    location.rating_set.create(user=request.user, rating=rating)
