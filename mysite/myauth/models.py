from django.db import models
from django.contrib.auth.models import User


def avatar_directory_path(instanse: "Profile", filename: str) -> str:
    return "accounts/profile_{pk}/avatar/{filename}".format(
        pk=instanse.pk,
        filename=filename,
    )

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=16, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to=avatar_directory_path)

    def __str__(self):
        return self.user
