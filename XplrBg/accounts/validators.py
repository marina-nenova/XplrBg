from django.core.exceptions import ValidationError


def check_name_contains_only_letters(value):
    if not value.isalpha():
        raise ValidationError("The name should contain only letters!")