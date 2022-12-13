from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views import generic as views

from XplrBg.accounts.forms import UserRegistrationForm, UserLoginForm, ProfileEditForm, ProfileDeleteForm
from XplrBg.accounts.models import UserProfile
from XplrBg.core.mixins.views_mixins import AuthorizationRequiredMixin, CheckIfOwnerMixin
from XplrBg.core.utils.locations_ustils import get_location_feature_image
from XplrBg.core.utils.posts_utils import apply_likes_count, apply_post_liked_by_users
from XplrBg.locations.models import Location
from XplrBg.posts.models import Post
from XplrBg.posts_common.forms import PostCommentForm

UserModel = get_user_model()


class UserRegistrationView(views.CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        if 'next' in self.request.GET:
            context['message'] = 'You need to be logged in to view this page.'
        return context


class UserLogoutView(auth_views.LogoutView):
    pass


class UserProfileDetailsView(LoginRequiredMixin, CheckIfOwnerMixin, views.DetailView):
    template_name = 'profiles/profile-details.html'
    model = UserProfile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        visited_locations_count = self.object.user.visited_locations.all().count()
        context['visited_locations_count'] = visited_locations_count
        return context


class UserProfileEditView(LoginRequiredMixin, AuthorizationRequiredMixin, views.UpdateView):
    template_name = 'profiles/profile-edit-page.html'
    model = UserProfile
    form_class = ProfileEditForm

    def get_success_url(self):
        return reverse_lazy('details profile', kwargs={
            'pk': self.request.user.pk,
        })


class UserProfileDeleteView(LoginRequiredMixin, AuthorizationRequiredMixin, views.DeleteView):
    template_name = 'profiles/profile-delete.html'
    model = UserProfile
    form_class = ProfileDeleteForm
    success_url = reverse_lazy('home')


class UserVisitedLocationsView(CheckIfOwnerMixin, LoginRequiredMixin, views.ListView):
    template_name = 'profiles/users-visited-locations.html'
    paginate_by = 9

    def get_queryset(self):
        visited_locations = Location.objects.filter(visitedlocations__user=self.kwargs['pk']).prefetch_related(
            'location_images')
        visited_locations = [get_location_feature_image(location) for location in visited_locations]
        return visited_locations


class UserWishlistLocationsView(CheckIfOwnerMixin, LoginRequiredMixin, views.ListView):
    template_name = 'profiles/users-wishlist-locations.html'
    paginate_by = 9

    def get_queryset(self):
        wishlist_locations = Location.objects.filter(wishlist__user=self.kwargs['pk']).prefetch_related(
            'location_images')
        wishlist_locations = [get_location_feature_image(location) for location in wishlist_locations]
        return wishlist_locations


class UserPostsView(CheckIfOwnerMixin, LoginRequiredMixin, views.ListView):
    template_name = 'profiles/users-posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostCommentForm()
        return context

    def get_queryset(self):
        queryset = Post.objects.filter(user_id=self.kwargs['pk'])
        queryset = [apply_likes_count(post) for post in queryset]
        queryset = [apply_post_liked_by_users(post, self.request.user) for post in queryset]
        return queryset
