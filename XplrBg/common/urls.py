from django.urls import path

from XplrBg.common.views import show_index

urlpatterns = (
    path('', show_index, name='home'),

)