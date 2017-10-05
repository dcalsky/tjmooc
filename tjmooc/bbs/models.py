from django.db import models
from django.core.validators import MaxLengthValidator, MinLengthValidator
from course.models import Course
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Forum(models.Model):
    name = models.TextField(validators=[MaxLengthValidator(20, '板块名字不能多于%(limit_value)s位!'),
                                        MinLengthValidator(3, '板块名字不能少于%(limit_value)s位')])
    owner = models.ForeignKey(User)
    course = models.ForeignKey(Course, null=True, blank=True)
    posts_length = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Floor(models.Model):
    title = models.TextField(validators=[MaxLengthValidator(50, '标题字数不能多于%(limit_value)s位!'),
                                         MinLengthValidator(6, '标题字数不能少于%(limit_value)s位')])
    content = models.TextField(error_messages={'blank': '帖子内容不能为空!'})  # Content of the post
    forum = models.ForeignKey(Forum)  # Overall forum: -1 else special forum
    owner = models.ForeignKey(User)  # Belong to someone

    def __str__(self):
        return self.title


class Post(models.Model):
    content = models.TextField(error_messages={'blank': '帖子内容不能为空!'})  # Content of the post
    owner = models.ForeignKey(User)  # Belong to someone
    belong = models.ForeignKey(Floor)
    floor = models.IntegerField(default=2)


