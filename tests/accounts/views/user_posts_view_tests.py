from django.urls import reverse_lazy

from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_visited_locations_for_user, create_wishlist_locations_for_user, \
    create_posts_for_user


class UserPostsViewTest(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'someone@abv.bg',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': '123456JD',
        'password2': '123456JD'
    }

    def test_user_posts__when_posts__expect_correct_count(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        create_posts_for_user(user, count=5)

        response = self.client.get(reverse_lazy('user posts', kwargs={'pk': user.pk}))

        object_list = response.context['object_list']

        self.assertEqual(5, len(object_list))

    def test_user_posts__when_no_posts__expect_empty(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('user posts', kwargs={'pk': user.pk}))

        object_list = response.context['object_list']

        self.assertEqual(0, len(object_list))