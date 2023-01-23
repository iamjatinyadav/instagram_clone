from django.db import models
# from user.models import User
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel
# Create your models here.


# for add username and phone field in User models

User = get_user_model()

class UserPersonalInfo(models.Model):
    user = models.OneToOneField('User', on_delete=models.CASCADE, null=True, blank=True, related_name="userpersonal")
    uniquename = models.CharField(max_length=40, unique=True)
    phone = models.CharField(max_length=40, unique=True)

    class Meta:
        app_label = 'user'


class FriendsRequest(TimeStampedModel):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name="receiver")
    action = models.BooleanField(default=False)

    class Meta:
        verbose_name = "friend request"
        verbose_name_plural = " friend requests"
        unique_together = (("sender", "receiver"))

    def __str__(self):
        return str(self.sender) + " send a request " + str(self.receiver)

