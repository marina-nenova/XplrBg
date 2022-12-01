from django.urls import path, include

from XplrBg.accounts.views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileEditView, \
    UserProfileDetailsView, UserVisitedLocationsView, UserWishlistLocationsView, UserProfileDeleteView

urlpatterns = (
    path('register/', UserRegistrationView.as_view(), name="register user"),
    path('login/', UserLoginView.as_view(), name="login user"),
    path('logout/', UserLogoutView.as_view(), name="logout user"),
    path('profile_edit/<int:pk>/', UserProfileEditView.as_view(), name='edit profile'),
    path('profile_delete/<int:pk>/', UserProfileDeleteView.as_view(), name='delete profile'),
    path('profile_details/<int:pk>/', include([
        path('', UserProfileDetailsView.as_view(), name='details profile'),
        path('visited-locations/', UserVisitedLocationsView.as_view(), name='user visited locations'),
        path('wishlist-locations/', UserWishlistLocationsView.as_view(), name='user wishlist locations'),
    ])

         ),
)

from XplrBg.accounts.signals import *
