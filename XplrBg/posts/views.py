from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views

from XplrBg.core.mixins.views_mixins import AuthorizationRequiredMixin
from XplrBg.locations.models import Location
from XplrBg.locations.views import rate_location
from XplrBg.posts.forms import PostCreateForm, PostEditForm, PostDeleteForm
from XplrBg.posts.models import Post


class CreatePostView(LoginRequiredMixin, views.CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        location_id = self.kwargs['loc_pk']
        location = Location.objects.get(id=location_id)
        form.instance.user = self.request.user
        form.instance.location = location
        location_rating = form.data.get('rate', None)
        if location_rating:
            rate_location(self.request, location_rating, location)
        return super().form_valid(form)


class EditPostView(LoginRequiredMixin, AuthorizationRequiredMixin, views.UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        location_rating = form.data.get('rate', None)
        if location_rating:
            rate_location(self.request, location_rating, self.object.location)
        form.save()
        return super().form_valid(form)


class DeletePostView(LoginRequiredMixin, AuthorizationRequiredMixin, views.DeleteView):
    model = Post
    form_class = PostDeleteForm
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('home')
