from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

UserModel = get_user_model()


class TestCaseBase(TestCase):

    def _create_user_and_login(self, user_data):
        response = self.client.post(
            reverse('register user'),
            data=user_data,
        )
        user = response.wsgi_request.user
        return user
