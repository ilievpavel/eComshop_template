from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

UserModel = get_user_model()


class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='users', blank=True)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
