from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from user.models import User
from course.models import Course


class Post(models.Model):
    title = models.CharField(validators=[MaxLengthValidator(50, '标题字数不能多于%(value)位!'),
                                         MinLengthValidator(6, '标题字数不能多于%(value)位')])  # Title of the post
    content = models.TextField(error_messages='帖子内容不能为空!')  # Content of the post
    user = models.ForeignKey(User)  # Belong to someone
    course = models.ForeignKey(Course, default=-1)  # Overall situation: -1 else special situation
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=-1)  # Top floor: -1
