from django.db import models
from user.models import User
# Create your models here.


# for add username and phone field in User models
class UserPersonalInfo(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True, blank=True, related_name="userpersonal")
    uniquename = models.CharField(max_length=40, unique=True)
    phone = models.CharField(max_length=40, unique=True)

    class Meta:
        app_label = 'user'



