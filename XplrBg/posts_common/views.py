from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from XplrBg.core.utils.posts_utils import get_post_url, get_user_liked_posts
from XplrBg.posts.models import Post
from XplrBg.posts_common.forms import PostCommentForm
from XplrBg.posts_common.models import PostLike


@login_required
def like_post(request, post_pk):
    user_liked_posts = get_user_liked_posts(post_pk, request.user.pk)

    if user_liked_posts:
        user_liked_posts.delete()
    else:
        PostLike.objects.create(
            post_id=post_pk,
            user_id=request.user.pk,
        )

    return redirect(get_post_url(request, post_pk))


@login_required
def comment_post(request, post_pk):
    post = Post.objects.filter(pk=post_pk) \
        .get()

    form = PostCommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()

    return redirect(get_post_url(request, post_pk))
