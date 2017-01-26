from django.db import models
from django.conf.global_settings import SECRET_KEY
from uuid import uuid4
from django.core.validators import MinLengthValidator, MaxLengthValidator


class User(models.Model):
    uuid = models.CharField(uuid=uuid4, primary_key=True)
    username = models.CharField(unique=True, validators=[MinLengthValidator(6, '用户名至少%(value)位!'),
                                                         MaxLengthValidator(16, '用户名至多%(value)位!')])
    password = models.CharField(MaxLengthValidator(20, '密码至多%(value)位!'), MinLengthValidator(6, '密码至少%(value)位!'))
    avatar = models.TextField(blank=True)
    role = models.IntegerField(default=1)
    nickname = models.CharField(blank=True, validators=[MaxLengthValidator(26, '昵称至多%(value)位!'),
                                                        MinLengthValidator(4, '昵称至少%(value)位!')])
