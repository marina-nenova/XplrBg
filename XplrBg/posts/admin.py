from django.contrib import admin

from XplrBg.posts.forms import PostCreateForm
from XplrBg.posts.models import Post
from XplrBg.posts_common.forms import PostCommentForm
from XplrBg.posts_common.models import PostComment, PostLike


class PostCommentsInline(admin.TabularInline):
    model = PostComment
    form = PostCommentForm

class PostLikeInline(admin.TabularInline):
    model = PostLike

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ordering = ('-updated_on',)
    list_display = ('user', 'updated_on', 'location')
    add_form = PostCreateForm
    list_filter = ('user', 'location')
    search_fields = ('user__email', 'location__name')
    sortable_by = ('id', 'user', 'location')
    inlines = (PostCommentsInline, PostLikeInline)
