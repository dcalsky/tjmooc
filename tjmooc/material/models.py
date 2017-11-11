from datetime import datetime

from django.db import models
from user.models import User


def homework_problem_path(instance, filename):
    return './upload/homework_{0}_problem_{1}'.format(instance.id, filename)


def homework_answer_path(instance, filename):
    return './upload/homework_{0}_answer_{1}'.format(instance.id, filename)


def homework_submit_path(instance, filename):
    return './upload/homework_{0}_submit_{1}'.format(instance.id, filename)


class Test(models.Model):
    deadline = models.DateTimeField(default=datetime.now)
    test_time = models.DateTimeField(default=datetime.now)
    chapter = models.ForeignKey('course.Chapter')


class TestSubmit(models.Model):
    answer = models.TextField(null=True)
    update_time = models.DateTimeField(default=datetime.now)
    test = models.ForeignKey(Test)
    user = models.ForeignKey(User)
    score = models.IntegerField(default=0)


class Homework(models.Model):
    file = models.TextField(null=True)  # homework description file URL
    title = models.CharField(max_length=100)
    desc = models.TextField()
    deadline = models.DateTimeField(default=datetime.now)
    chapter = models.ForeignKey('course.Chapter')


class HomeworkSubmit(models.Model):
    file = models.TextField(null=True)  # homework answer file URL
    homework = models.ForeignKey(Homework)
    user = models.ForeignKey(User)
    update_time = models.DateTimeField(default=datetime.now)


class Question(models.Model):
    type = models.CharField(max_length=20)
    score = models.IntegerField()
    desc = models.TextField()
    options = models.TextField(null=True)
    right_answer = models.TextField()
    test = models.ForeignKey(Test)


class Video(models.Model):
    title = models.TextField(help_text='标题')
    description = models.TextField(help_text='说明')
    unit = models.ForeignKey('course.Unit', null=True)
    upload_time = models.DateTimeField(auto_now_add=True, help_text='创建时间', blank=True)
    url = models.URLField(help_text='链接')
    teacher = models.ForeignKey(User)
