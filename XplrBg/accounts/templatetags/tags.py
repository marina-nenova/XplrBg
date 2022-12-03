from django.template import Library

from XplrBg.accounts.models import UserProfile

register = Library()


@register.inclusion_tag('tags/avatar.html', name='show_avatar')
def show_avatar(user):
    profile = UserProfile.objects.get(pk=user.id)
    return {'profile': profile}
