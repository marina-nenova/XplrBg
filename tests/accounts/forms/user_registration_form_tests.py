from django.contrib.auth import get_user_model
from XplrBg.accounts.forms import UserRegistrationForm
from tests.accounts.BaseTestCase import TestCaseBase

UserModel = get_user_model()


class UserRegistrationFormTests(TestCaseBase):
    VALID_USER_DATA = {
        'email': 'someone@abv.bg',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': '123456JD',
        'password2': '123456JD'
    }

    INVALID_USER_DATA = {
        'email': 'someone@',
        'first_name': 'John',
        'last_name': 'Doe',
        'password1': '123456JD',
        'password2': '123456jd'
    }

    def test_user_registration_form_with_valid_data__form_valid_is_True(self):
        form = UserRegistrationForm(data=self.VALID_USER_DATA)
        self.assertTrue(form.is_valid())

    def test_user_registration_form_with_invalid_data__form_valid_is_False(self):
        form = UserRegistrationForm(data=self.INVALID_USER_DATA)
        self.assertFalse(form.is_valid())

    def test_user_registration_form_with_email_already_used_sends_correct_message(self):
        self._create_user_and_login(self.VALID_USER_DATA)

        form = UserRegistrationForm(data=self.VALID_USER_DATA)

        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['email'], ["User with this email already exists"])

    def test_user_registration_form_with_passwords_mismatch_sends_correct_message(self):
        form = UserRegistrationForm(data=self.INVALID_USER_DATA)

        self.assertFalse(form.is_valid())
        self.assertEquals(form.errors['password2'], ["The passwords don't match"])
