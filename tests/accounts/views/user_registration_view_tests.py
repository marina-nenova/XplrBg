from django.urls import reverse

from XplrBg.accounts.models import UserProfile
from tests.accounts.BaseTestCase import TestCaseBase


class UserRegistrationViewTests(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'someone@abv.bg',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': '123456JD',
        'password2': '123456JD'
    }

    def test_sign_up__when_valid_data__login_user(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA,
        )
        self.assertEqual(self.VALID_USER_DATA['email'], response.wsgi_request.user.email)

    def test_register_user__when_valid_data__creates_profile(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA,
        )
        # self.assertEqual(user.profile, Profile.objects.get(user=new_user))
        self.assertIsNotNone(UserProfile.objects.get(user=response.wsgi_request.user))
