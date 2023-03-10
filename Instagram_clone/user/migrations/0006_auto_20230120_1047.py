# Generated by Django 3.2.16 on 2023-01-20 10:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_userpersonalinfo_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userpersonalinfo',
            old_name='username',
            new_name='uniquename',
        ),
        migrations.AlterField(
            model_name='userpersonalinfo',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userpersonal', to=settings.AUTH_USER_MODEL),
        ),
    ]
