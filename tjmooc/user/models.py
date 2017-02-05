from django.db import models
from django.conf.global_settings import SECRET_KEY
from uuid import uuid4
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    avatar = models.TextField(blank=True)
    phone = models.TextField(blank=True)
