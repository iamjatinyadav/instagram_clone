from django.db import models
from user.models import User
# Create your models here.
import user


class UserPersonalInfo(models.Model):
    username = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

    class Meta:
        app_label = 'user'


