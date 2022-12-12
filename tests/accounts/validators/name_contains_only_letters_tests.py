from django.core.exceptions import ValidationError
from django.test import TestCase

from XplrBg.accounts.validators import check_name_contains_only_letters


class NameHasOnlyLettersValidatorTests(TestCase):

    def test_create_name__with_only_letters__expect_ok(self):
        name = 'John'
        check_name_contains_only_letters(name)

    def test_create_name__with_numbers__expect_exception(self):
        with self.assertRaises(ValidationError) as context:
            check_name_contains_only_letters('123456789')

        self.assertIsNotNone(context.exception, msg="The name should contain only letters!")
