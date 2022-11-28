from cloudinary.forms import CloudinaryFileField
from django import forms

from XplrBg.core.mixins.form_mixins import SetFieldsClassFormMixin
from XplrBg.posts.models import Post


class PostCreateForm(SetFieldsClassFormMixin, forms.ModelForm):
    UPLOAD_FOLDER = 'XplrBg/Posts/Images'

    class Meta:
        model = Post
        fields = ('text', 'image')

    image = CloudinaryFileField(
        options={
            'use_filename': True,
            'folder': UPLOAD_FOLDER,
        }
    )


class PostEditForm(SetFieldsClassFormMixin, forms.ModelForm):
    UPLOAD_FOLDER = 'XplrBg/Posts/Images'

    class Meta:
        model = Post
        fields = ('text', 'image')

    image = CloudinaryFileField(
        options={
            'use_filename': True,
            'folder': UPLOAD_FOLDER,
        }
    )