from tests.accounts.BaseTestCase import TestCaseBase


class AppUserModelTests(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'someone@abv.bg',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': '123456JD',
        'password2': '123456JD'
    }

    def test_app_user__username_property_returns_correct(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        self.assertEqual('John Doe', user.username)
