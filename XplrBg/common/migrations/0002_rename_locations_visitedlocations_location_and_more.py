# Generated by Django 4.1.3 on 2022-11-30 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitedlocations',
            old_name='locations',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='wishlist',
            old_name='locations',
            new_name='location',
        ),
    ]
