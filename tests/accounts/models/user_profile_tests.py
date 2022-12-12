from tests.accounts.BaseTestCase import TestCaseBase


class UserProfileModelTests(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'someone@abv.bg',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': '123456JD',
        'password2': '123456JD'
    }

    def test_user_profile__get_full_name_property_returns_correct(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        self.assertEqual('John Doe', user.user_profile.get_full_name)
