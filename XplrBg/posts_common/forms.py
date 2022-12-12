from django import forms

from XplrBg.core.mixins.form_mixins import SetFieldsClassFormMixin
from XplrBg.posts_common.models import PostComment


class PostCommentForm(SetFieldsClassFormMixin, forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(attrs={'placeholder': "Write your comment here"}),
        }
