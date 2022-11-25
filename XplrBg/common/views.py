from django.shortcuts import render

def show_index(request):
    context = {'user': request.user}
    return render(request, 'home.html', context)
