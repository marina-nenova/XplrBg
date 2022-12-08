from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.views import generic as views

from XplrBg.accounts.models import UserProfile
from XplrBg.core.utils.accounts_utils import is_owner
from XplrBg.locations.models import Location


class AuthorizationRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.user


class FilteredLocationsView(views.ListView):
    filterset_class = None

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class UserVisitedAndWishlistLocationsMixin(object):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['visited_locations'] = Location.objects.filter(visitedlocations__user=self.request.user)
        context['wishlist_locations'] = Location.objects.filter(wishlist__user=self.request.user)

        return context


class CheckIfOwnerMixin(object):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = get_object_or_404(UserProfile, pk=self.kwargs['pk'])
        context['is_owner'] = is_owner(self.request, user_profile)
        return context