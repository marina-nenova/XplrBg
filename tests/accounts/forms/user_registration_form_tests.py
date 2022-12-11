from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class UserRegistrationFormTests(TestCase):
    VALID_USER_DATA = {
        'email': 'someone@abv.bg',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': '123456JD',
        'password2': '123456JD'
    }




