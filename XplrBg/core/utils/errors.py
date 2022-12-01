from django.shortcuts import render


def error400(request):
    return render(request, 'errors/400.html', status=400)


def error403(request):
    return render(request, 'errors/403.html', status=403)


def error404(request):
    return render(request, 'errors/404.html', status=404)


def internal_server_error(request, exception):
    return render(request, "errors/500.html", status=500)
