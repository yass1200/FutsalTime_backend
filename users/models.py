from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    profile_picture = models.URLField(blank=True)

    # Following system: users can follow other users
    following = models.ManyToManyField("self", symmetrical=False, related_name="followers", blank=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self) -> str:
        return self.username
