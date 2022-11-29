from XplrBg.locations.models import Rating


def get_location_feature_image(location):
    location.feature_image = location.location_images.get(is_feature=True)
    return location


def get_location_user_rating(location, user):
    rating = Rating.objects.filter(location=location, user_id=user.id).first()
    location.user_rating = rating.rating if rating else 0
    return location


# def location_visited_by_user(location, user):
#     locations_visited_by_user = VisitedLocations.objects.filter(user_id=user.id)
#     location.visited_by_user = location in locations_visited_by_user
#     return location
#
#
# def location_in_users_wishlist(location, user):
#     locations_wished_by_user = Wishlist.objects.filter(user_id=user.id)
#     location.wished_by_user = location in locations_wished_by_user
#     return location
