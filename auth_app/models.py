from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    phoneNumber = models.CharField(max_length=15)

    def __str__(self):
        return self.username
