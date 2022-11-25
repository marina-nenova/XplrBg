# Generated by Django 4.1.3 on 2022-11-25 14:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinValueValidator(2)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, validators=[django.core.validators.MinValueValidator(2)]),
        ),
    ]