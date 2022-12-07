from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic as views

from XplrBg.core.mixins.views_mixins import FilteredLocationsView, UserVisitedAndWishlistLocationsMixin
from XplrBg.locations.filters import LocationsFilter
from XplrBg.locations.models import Location, Rating


class ShowAllLocations(UserVisitedAndWishlistLocationsMixin, LoginRequiredMixin, FilteredLocationsView):
    context_object_name = 'all_locations'
    template_name = 'locations/locations-list.html'
    model = Location
    filterset_class = LocationsFilter
    paginate_by = 9


class LocationDetails(UserVisitedAndWishlistLocationsMixin, LoginRequiredMixin, views.DetailView):
    model = Location
    template_name = 'locations/location-details.html'
    context_object_name = 'location'


class TopTenLocationsView(views.TemplateView):
    template_name = 'locations/top-ten-locations.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(TopTenLocationsView, self).get_context_data(**kwargs)

        context['top_ten_visited'] = sorted(Location.objects.all(), key=lambda a: -a.times_visited)[:10]
        context['top_ten_rated'] = sorted(Location.objects.all(), key=lambda a: -a.average_rating)[:10]
        return context


def rate_location(request, rating: int, location):
    Rating.objects.filter(location=location, user=request.user).delete()
    location.rating_set.create(user=request.user, rating=rating)
