def is_owner(request, obj):
    return request.user.pk == obj.user.pk