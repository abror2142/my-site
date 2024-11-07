from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    first_name = None
    last_name = None


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pictureURL = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.user.username