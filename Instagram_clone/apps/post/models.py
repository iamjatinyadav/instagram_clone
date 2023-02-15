from django.db import models

from django.contrib.auth import get_user_model
from django_extensions.db.models import TimeStampedModel


User = get_user_model()


def user_post_directory_path(instance, filename):
    return 'UserPost/{0}/{1}'.format(instance.user.userpersonal.uniquename, filename)


class Post(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    image = models.ImageField(upload_to=user_post_directory_path)
    image_bio = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["-id"]
        verbose_name = "UserPost"
        verbose_name_plural = "UserPosts"

    def __str__(self):
        return str(self.user) + " add a picture " + str(self.pk)


class UserSaved(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_saved")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="posts")

    class Meta:
        ordering = ["-id"]
        unique_together = (("user", "post"),)
        verbose_name = "UserSaved"
        verbose_name_plural = "UserSaved"

    def __str__(self):
        return str(self.pk)

