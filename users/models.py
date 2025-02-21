from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False)
    email_confirmed = models.BooleanField(default=False)
    dob = models.DateField(null=False, blank=False, default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "dob"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email
