from XplrBg.posts_common.models import PostLike


def get_post_url(request, post_id):
    return request.META['HTTP_REFERER'] + f'#post-{post_id}'


def apply_likes_count(post):
    post.likes_count = post.postlike_set.count()
    return post


def get_user_liked_posts(post_pk, user_pk):
    user_liked_posts = PostLike.objects \
        .filter(post_id=post_pk, user_id=user_pk)
    return user_liked_posts


def apply_post_liked_by_users(post, user):
    post_liked_by_user = get_user_liked_posts(post.pk, user.pk)

    post.liked_by_user = True if post_liked_by_user else False
    return post
