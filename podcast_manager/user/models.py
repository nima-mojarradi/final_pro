from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return self.username
