from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models


class User(AbstractUser):
    username = models.CharField(
        max_length=150,
        unique=True,
        validators=(RegexValidator(regex=r'^[\w.@+-]+\Z'),)
    )
    email = models.EmailField(unique=True)
    user_url = models.URLField(
        max_length=200,
        unique=True,
    )

    def __str__(self):
        return self.username

    class Meta:
        ordering = ('username',)
