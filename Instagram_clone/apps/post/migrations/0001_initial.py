# Generated by Django 3.2.16 on 2023-02-08 05:05

import apps.post.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('image', models.ImageField(upload_to=apps.post.models.user_post_directory_path)),
                ('image_bio', models.CharField(blank=True, max_length=200, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserPost',
                'verbose_name_plural': 'UserPosts',
            },
        ),
    ]
