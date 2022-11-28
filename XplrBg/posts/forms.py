from cloudinary.forms import CloudinaryFileField
from django import forms

from XplrBg.posts.models import Post


class PostCreateForm(forms.ModelForm):
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