from django.db import models
from django.conf.global_settings import SECRET_KEY
from uuid import uuid4
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.TextField(unique=True)
    nickname = models.TextField(blank=True)
    avatar = models.TextField(blank=True)
    phone = models.TextField(blank=True)

    USERNAME_FIELD = 'username'
