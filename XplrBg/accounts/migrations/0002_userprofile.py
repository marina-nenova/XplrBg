# Generated by Django 4.1.3 on 2022-11-25 13:58

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('first_name', models.CharField(max_length=30, validators=[django.core.validators.MinValueValidator(2)])),
                ('last_name', models.CharField(max_length=30, validators=[django.core.validators.MinValueValidator(2)])),
                ('lives_at', models.CharField(blank=True, max_length=50, null=True, validators=[django.core.validators.MinValueValidator(2)])),
                ('profile_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user_profile', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
