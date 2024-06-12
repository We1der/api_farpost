from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
    )
    email = models.EmailField(
        blank=True,
    )
    user_url = models.URLField(
        max_length=200,
        blank=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)
