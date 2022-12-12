import django_filters

from XplrBg.locations.models import Location


class LocationsFilter(django_filters.FilterSet):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.form.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.form.fields['name__icontains'].label = "Name"

    class Meta:
        model = Location
        fields = {
            'name': ['icontains'],
            'region': ['exact'],
            'category': ['exact'],
        }
