from uuid import uuid4
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class User(models.Model):
    ROLE_CHOICES = (
        (0, 'Administrator'),
        (1, 'Teacher'),
        (2, 'Student')
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    username = models.TextField(unique=True,
                                validators=[MinLengthValidator(6, '用户名至少%(value)位!'),
                                            MaxLengthValidator(16, '用户名至多%(value)位!')])
    password = models.TextField(validators=[MaxLengthValidator(20, '密码至多%(value)位!'),
                                            MinLengthValidator(6, '密码至少%(value)位!')])
    mail = models.TextField(blank=True)
    role = models.IntegerField(default=2, choices=ROLE_CHOICES)
    nickname = models.TextField(blank=True,
                                validators=[MaxLengthValidator(26, '昵称至多%(value)位!'),
                                            MinLengthValidator(4, '昵称至少%(value)位!')])
