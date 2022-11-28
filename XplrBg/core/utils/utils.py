
def is_owner(request, obj):
    return request.user.pk == obj.user.pk


def get_location_feature_image(locations):
    for location in locations:
        location.feature_image = location.location_images.get(is_feature=True)
    return locations
