# Generated by Django 4.1.3 on 2022-12-10 13:19

import XplrBg.accounts.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_userprofile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), XplrBg.accounts.validators.check_name_contains_only_letters]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinLengthValidator(2), XplrBg.accounts.validators.check_name_contains_only_letters]),
        ),
    ]