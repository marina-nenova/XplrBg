from django.urls import path

from XplrBg.posts.views import CreatePostView, EditPostView, DeletePostView

urlpatterns = (
    path('create/<int:loc_pk>/', CreatePostView.as_view(), name='create post'),
    path('edit/<int:pk>/', EditPostView.as_view(), name='edit post'),
    path('delete/<int:pk>/', DeletePostView.as_view(), name='delete post'),
)

from XplrBg.posts.signals import *