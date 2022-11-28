from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic as views

from XplrBg.accounts.forms import UserRegistrationForm, UserLoginForm, ProfileEditForm
from XplrBg.accounts.models import UserProfile
from XplrBg.core.utils.utils import is_owner, get_location_feature_image
from XplrBg.locations.models import Location

UserModel = get_user_model()


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(SuccessMessageMixin, auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def get_success_url(self):
        return reverse_lazy('home')


class UserLogoutView(auth_views.LogoutView):
    pass


class UserProfileDetailsView(LoginRequiredMixin, views.DetailView):
    template_name = 'profiles/profile-details.html'
    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visited_locations = Location.objects.filter(visitedlocations__user_id=self.object.user_id)
        wishlist_locations = Location.objects.filter(wishlist__user_id=self.object.user_id)

        for loc_list in [visited_locations, wishlist_locations]:
            get_location_feature_image(loc_list)

        context['is_owner'] = is_owner(self.request, self.object)
        context['visited_locations'] = visited_locations
        context['wishlist_locations'] = wishlist_locations

        return context


class UserProfileEditView(LoginRequiredMixin, views.UpdateView):
    template_name = 'profiles/profile-edit-page.html'
    model = UserProfile
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={
            'pk': self.request.user.pk,
        })


class UserVisitedLocationsView(LoginRequiredMixin, views.ListView):
    template_name = 'profiles/users-visited-locations.html'

    def get_queryset(self):
        visited_locations = Location.objects.filter(visitedlocations__user=self.kwargs['pk']).prefetch_related('location_images')
        for location in visited_locations:
            location.feature_image = location.location_images.get(is_feature=True)
        return visited_locations


class UserWishlistLocationsView(LoginRequiredMixin, views.ListView):
    template_name = 'profiles/users-wishlist-locations.html'

    def get_queryset(self):
        wishlist_locations = Location.objects.filter(wishlist__user=self.kwargs['pk']).prefetch_related('location_images')
        for location in wishlist_locations:
            location.feature_image = location.location_images.get(is_feature=True)
        return wishlist_locations