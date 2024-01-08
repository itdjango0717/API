from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.phone}-->{self.adress}"
