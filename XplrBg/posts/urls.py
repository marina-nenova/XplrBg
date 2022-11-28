from django.urls import path

from XplrBg.posts.views import CreatePostView

urlpatterns = (
    path('create/<int:loc_pk>/', CreatePostView.as_view(), name='create post'),
)