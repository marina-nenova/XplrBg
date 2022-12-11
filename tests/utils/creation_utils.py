from XplrBg.common.models import VisitedLocations, Wishlist
from XplrBg.locations.models import Location, LocationImage
from XplrBg.posts.models import Post


def create_visited_locations_for_user(user, count):
    result = [VisitedLocations(
        location=create_location(f'Location {i + 1}'),
        user=user
    ) for i in range(count)]

    [l.save() for l in result]

    return result


def create_wishlist_locations_for_user(user, count):
    result = [Wishlist(
        location=create_location(f'Location {i + 1}'),
        user=user
    ) for i in range(count)]

    [l.save() for l in result]

    return result


def create_posts_for_user(user, count):
    result = [Post(
        location=create_location(f'Location {i + 1}'),
        user=user,
        text='Some Text'
    ) for i in range(count)]

    [p.save() for p in result]

    return result


def create_location(name):
    location = Location(
        name=name,
        short_description='Short description',
        details='details'
    )
    location.save()
    create_location_image(location)
    return location


def create_location_image(location):
    location_image = LocationImage(
        location=location,
        is_feature=True,
        image='staticfiles/images/profile-default-image.webp'
    )
    location_image.save()
