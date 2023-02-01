from django.db import models
# from user.models import User
from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _

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


def user_directory_path(instance, filename):
    return 'profilePicture/{0}/{1}'.format(instance.user.userpersonal.uniquename, filename)


class UserProfilePic(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile_pic")
    profile_pic = models.FileField(upload_to=user_directory_path)

    class Meta:
        verbose_name = "UserProfilePics"
        verbose_name_plural = "UserProfilePics"


class UserProfile(TimeStampedModel):
    class Gender(models.TextChoices):
        MALE = "MALE", _('Male')
        FEMALE = "FEMALE", _('Female')
        OTHER = "OTHER", _('Other')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile_infos")
    website = models.CharField(max_length=200)
    gender = models.CharField(choices=Gender.choices, max_length=10, default=Gender.MALE)
    bio = models.TextField(max_length=200)
    flag = models.BooleanField(default=True)

    class Meta:
        verbose_name = "UserProfileInfo"
        verbose_name_plural = "UserProfileInfo"

    def __str__(self):
        return str(self.user) + "Add detail"






