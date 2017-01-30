from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from user.models import User
from course.models import Course


class Forum(models.Model):
    name = models.TextField(validators=[MaxLengthValidator(20, '板块名字不能多于%(value)位!'),
                                        MinLengthValidator(6, '板块名字不能少于%(value)位')])
    moderator = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    posts_length = models.IntegerField(default=0)


class Post(models.Model):
    title = models.TextField(validators=[MaxLengthValidator(50, '标题字数不能多于%(value)位!'),
                                         MinLengthValidator(6, '标题字数不能少于%(value)位')])  # Title of the post
    content = models.TextField(error_messages={'blank': '帖子内容不能为空!'})  # Content of the post
    user = models.ForeignKey(User)  # Belong to someone
    parent = models.ForeignKey('self', on_delete=models.CASCADE, default=-1)  # Top floor: -1
    forum = models.ForeignKey(Forum)  # Overall forum: -1 else special forum

