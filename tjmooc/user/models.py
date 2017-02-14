from django.db import models
from django.conf.global_settings import SECRET_KEY
from uuid import uuid4
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.TextField(unique=True,
                                validators=[MinLengthValidator(6, '用户名至少%(limit_value)s位!'),
                                            MaxLengthValidator(16, '用户名至多%(limit_value)s位!')])
    password = models.TextField(validators=[MinLengthValidator(6, '密码至少%(limit_value)s位!'),
                                            MaxLengthValidator(120, '密码至多%(limit_value)s位!')])
    email = models.TextField(blank=True)
    nickname = models.TextField(blank=True,
                                validators=[MaxLengthValidator(26, '昵称至多%(limit_value)s位!'),
                                            MinLengthValidator(4, '昵称至少%(limit_value)s位!')])
    avatar = models.TextField(blank=True)
    phone = models.TextField(blank=True)

    USERNAME_FIELD = 'username'
