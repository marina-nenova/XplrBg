from django.urls import path

from XplrBg.accounts.views import UserRegistrationView, UserLoginView, UserLogoutView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name="register user"),
    path('login/', UserLoginView.as_view(), name="login user"),
    path('logout/', UserLogoutView.as_view(), name="logout user"),
)

from XplrBg.accounts.signals import *