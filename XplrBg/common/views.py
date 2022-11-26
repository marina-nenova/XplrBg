from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from XplrBg.common.models import Wishlist, VisitedLocations
from XplrBg.locations.models import Location

UserModel = get_user_model()

def show_index(request):
    context={
        'all_users': UserModel.objects.all()
    }
    return render(request, 'home.html', context)


@login_required
def add_to_wishlist(request, loc_pk):
    location = get_object_or_404(Location, id=loc_pk)
    if Wishlist.objects.filter(user_id=request.user.id, locations_id=loc_pk).exists():
        remove_from_wishlist(request.user, location)
    else:
        Wishlist.objects.create(user_id=request.user.id, locations_id=location.id)

    return redirect(request.META["HTTP_REFERER"] + f'#{loc_pk}')


def remove_from_wishlist(current_user, location):
    Wishlist.objects.get(user=current_user, locations=location).delete()


@login_required
def mark_as_visited(request, loc_pk):
    location = get_object_or_404(Location, id=loc_pk)

    if not VisitedLocations.objects.filter(user_id=request.user.id, locations_id=loc_pk).exists():
        VisitedLocations.objects.create(locations_id=location.id, user_id=request.user.id)
        remove_from_wishlist(request.user, location)

    return redirect(request.META["HTTP_REFERER"] + f'#{loc_pk}')