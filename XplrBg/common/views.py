from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views import generic as views
from XplrBg.common.models import Wishlist, VisitedLocations
from XplrBg.core.utils.posts_utils import apply_likes_count, apply_post_liked_by_users
from XplrBg.locations.models import Location
from XplrBg.posts.models import Post


UserModel = get_user_model()


class ShowAllPosts(LoginRequiredMixin, views.ListView):
    model = Post
    template_name = 'feed.html'
    ordering = ('-updated_on',)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ShowAllPosts, self).get_context_data(object_list=None, **kwargs)
        return context

    def get_queryset(self):
        queryset = super(ShowAllPosts, self).get_queryset()
        query = self.__get_query()
        if query:
            queryset = queryset.filter(location__name__icontains=query)

        queryset = [apply_likes_count(post) for post in queryset]
        queryset = [apply_post_liked_by_users(post, self.request.user) for post in queryset]

        return queryset

    def __get_query(self):
        query = self.request.GET.get('query', None)
        return query


@login_required
def add_to_wishlist(request, loc_pk):
    location = get_object_or_404(Location, id=loc_pk)
    if Wishlist.objects.filter(user_id=request.user.id, locations_id=loc_pk).exists():
        remove_from_wishlist(request.user, location)
    else:
        Wishlist.objects.create(user_id=request.user.id, locations_id=location.id)

    return redirect(request.META["HTTP_REFERER"] + f'#{loc_pk}')


def remove_from_wishlist(current_user, location):
    if Wishlist.objects.filter(user=current_user, locations=location):
        Wishlist.objects.get(user=current_user, locations=location).delete()


@login_required
def mark_as_visited(request, loc_pk):
    location = get_object_or_404(Location, id=loc_pk)

    if not VisitedLocations.objects.filter(user_id=request.user.id, locations_id=loc_pk).exists():
        VisitedLocations.objects.create(locations_id=location.id, user_id=request.user.id)
        remove_from_wishlist(request.user, location)

    return redirect(request.META["HTTP_REFERER"] + f'#{loc_pk}')