from django.urls import path

from XplrBg.common.views import show_index, add_to_wishlist, mark_as_visited, ShowAllPosts

urlpatterns = (
    path('', ShowAllPosts.as_view(), name='home'),
    path('add_to_wishlist/<int:loc_pk>/', add_to_wishlist, name='add to wishlist'),
    path('mark_as_visited/<int:loc_pk>/', mark_as_visited, name='mark as visited'),

)