from django.urls import reverse_lazy

from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_visited_locations_for_user


class UserDetailsViewTests(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'someone@abv.bg',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': '123456JD',
        'password2': '123456JD'
    }

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details profile', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        profile_user = self._create_user_and_login({
            'email': 'someone2@abv.bg',
            'first_name': 'Jane',
            'last_name': 'Doe',
            'password1': '123456JD',
            'password2': '123456JD'
        })

        self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details profile', kwargs={'pk': profile_user.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_user_details__when_no_visited_locations__expect_empty(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details profile', kwargs={'pk': user.pk}))

        self.assertEqual(0, response.context['visited_locations_count'])

    def test_user_details__when_visited_locations__expect_correct_count(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        create_visited_locations_for_user(user, count=5)

        response = self.client.get(reverse_lazy('details profile', kwargs={'pk': user.pk}))

        self.assertEqual(5, response.context['visited_locations_count'])
