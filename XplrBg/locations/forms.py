from cloudinary.forms import CloudinaryFileField
from django import forms

from XplrBg.locations.models import LocationImage


class LocationImageForm(forms.ModelForm):
    IMAGE_WIDTH = 1000
    IMAGE_HEIGHT = 500
    UPLOAD_FOLDER = 'XplrBg/Locations/Images'

    class Meta:
        model = LocationImage
        fields = ('image', 'is_feature')

    image = CloudinaryFileField(
        options={
            'use_filename': True,
            'folder': UPLOAD_FOLDER,
            'crop': 'limit', 'width': IMAGE_WIDTH, 'height': IMAGE_HEIGHT,
        }
    )


class CreateLocationForm(forms.ModelForm):
    class Meta:
        fields = ('name', 'short_description', 'details', 'town', 'category', 'region')
