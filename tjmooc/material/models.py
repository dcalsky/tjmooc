from django.db import models
from user.models import User
from course.models import Chapter, Unit


def homework_problem_path(instance, filename):
    return './upload/homework_{0}_problem_{1}'.format(instance.id, filename)


def homework_answer_path(instance, filename):
    return './upload/homework_{0}_answer_{1}'.format(instance.id, filename)


def homework_submit_path(instance, filename):
    return './upload/homework_{0}_submit_{1}'.format(instance.id, filename)


class Homework(models.Model):
    chapter = models.ForeignKey(Chapter, related_name='homeworks')
    title = models.CharField(max_length=50, unique=True)
    introduction = models.TextField()
    problem_file = models.FileField(upload_to=homework_problem_path)
    answer_file = models.FileField(upload_to=homework_answer_path)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.title


class HomeworkSubmit(models.Model):
    homework_id = models.ForeignKey(Homework)
    submit_user_id = models.ForeignKey(User, related_name='homework_submit_user_id')
    judge_user_id = models.ForeignKey(User, related_name='homework_judge_user_id', null = True, blank = True)
    comment = models.TextField(null=True, blank = True)
    score = models.IntegerField(null=True, blank = True)
    submit_time = models.DateTimeField(auto_now_add=True)
    judge_time = models.DateTimeField(auto_now=True, null = True, blank = True)
    submit_file = models.FileField(upload_to=homework_submit_path)

    def __str__(self):
        return self.homework_id.title + " " + self.submit_user_id.name


class Test(models.Model):
    title = models.CharField(max_length=50)
    introduction = models.TextField()
    answer = models.CharField(max_length=10, default='')
    deadline = models.DateTimeField()
    unit = models.ForeignKey(Unit)


class TestSubmit(models.Model):
    test = models.ForeignKey(Test)
    submit_user = models.ForeignKey(User, related_name='test_submit_user_id')
    submit_time = models.DateTimeField(auto_now_add=True)
    submit = models.CharField(max_length=10)
    score = models.IntegerField(null=True)


class Video(models.Model):
    title = models.TextField(help_text='标题')
    description = models.TextField(help_text='说明')
    upload_time = models.DateTimeField(auto_now_add=True, help_text='创建时间', blank=True)
    url = models.URLField(help_text='链接')
    teacher = models.ForeignKey(User)
