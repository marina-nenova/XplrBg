from django.urls import path

from XplrBg.accounts.views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileEditView, \
    UserProfileDetailsView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name="register user"),
    path('login/', UserLoginView.as_view(), name="login user"),
    path('logout/', UserLogoutView.as_view(), name="logout user"),
    path('profile_edit/<int:pk>/', UserProfileEditView.as_view(), name='edit profile'),
    path('profile_details/<int:pk>/', UserProfileDetailsView.as_view(), name='details profile'),
)

from XplrBg.accounts.signals import *