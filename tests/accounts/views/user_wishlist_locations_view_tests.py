from django.urls import reverse_lazy

from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_wishlist_locations_for_user


class UserWishlistLocationsViewTest(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'someone@abv.bg',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': '123456JD',
        'password2': '123456JD'
    }

    def test_user_wishlist_locations__when_wishlist_locations__expect_correct_count(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        create_wishlist_locations_for_user(user, count=5)

        response = self.client.get(reverse_lazy('user wishlist locations', kwargs={'pk': user.pk}))

        object_list = response.context['object_list']

        self.assertEqual(5, len(object_list))

    def test_user_wishlist_locations__when_no_wishlist_locations__expect_empty(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('user wishlist locations', kwargs={'pk': user.pk}))

        object_list = response.context['object_list']

        self.assertEqual(0, len(object_list))

    def test_user_wishlist_locations__when_wishlist_locations_11__expect_page_1_has_9_locations(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        wishlist_locations = create_wishlist_locations_for_user(user, count=11)
        locations = [vl.location for vl in wishlist_locations]

        response = self.client.get(reverse_lazy('user wishlist locations', kwargs={'pk': user.pk}))

        object_list = response.context['object_list']

        self.assertListEqual(locations[:9], list(response.context['object_list']))
        self.assertEqual(9, len(object_list))

    def test_user_wishlist_locations__when_wishlist_locations_11__expect_page_2_has_2_locations(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        wishlist_locations = create_wishlist_locations_for_user(user, count=11)
        locations = [vl.location for vl in wishlist_locations]

        response = self.client.get(reverse_lazy('user wishlist locations', kwargs={'pk': user.pk}),
                                   data={'page': 2})

        object_list = response.context['object_list']

        self.assertListEqual(locations[9:11], list(response.context['object_list']))
        self.assertEqual(2, len(object_list))
