from django.urls import path

from XplrBg.posts.views import CreatePostView, EditPostView

urlpatterns = (
    path('create/<int:loc_pk>/', CreatePostView.as_view(), name='create post'),
    path('edit/<int:pk>/', EditPostView.as_view(), name='edit post'),
)

from XplrBg.posts.signals import *