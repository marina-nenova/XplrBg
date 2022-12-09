from XplrBg.common.models import Wishlist


def get_location_feature_image(location):
    location.feature_image = location.location_images.get(is_feature=True)
    return location


def get_location_url(request, loc_pk):
    return request.META["HTTP_REFERER"] + f'#{loc_pk}'


def remove_from_wishlist(current_user, location):
    if Wishlist.objects.filter(user=current_user, location=location):
        Wishlist.objects.get(user=current_user, location=location).delete()
