# Generated by Django 4.1.3 on 2022-11-30 13:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_text'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts_common', '0002_rename_photo_postlike_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=300)),
                ('post', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='posts.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
