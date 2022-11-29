from django.urls import path

from XplrBg.posts_common.views import like_post

urlpatterns = (
    path('like-post/<int:post_pk>', like_post, name='like post'),

)