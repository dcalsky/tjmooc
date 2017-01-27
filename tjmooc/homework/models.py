from django.db import models
from user.models import User

def homework_problem_path(instance, filename):
    return './upload/homework_{0}_problem_{1}'.format(instance.id, filename)


def homework_answer_path(instance, filename):
    return './upload/homework_{0}_answer_{1}'.format(instance.id, filename)


def homework_submit_path(instance, filename):
    return './upload/homework_{0}_submit_{1}'.format(instance.id, filename)



class Homework(models.Model):
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
    judge_user_id = models.ForeignKey(User, related_name='homework_judge_user_id')
    comment = models.TextField(null=True)
    score = models.IntegerField(null=True)
    submit_time = models.DateTimeField(auto_now_add=True)
    judge_time = models.DateTimeField(auto_now=True)
    submit_file = models.FileField(upload_to=homework_submit_path)



class Test(models.Model):
    title = models.CharField(max_length=50, unique=True)
    introduction = models.TextField()
    problem_file = models.FileField(upload_to=homework_problem_path)
    answer_file = models.FileField(upload_to=homework_answer_path)
    deadline = models.DateTimeField()


class TestSubmit(models.Model):
    test_id = models.ForeignKey(Test)
    submit_user_id = models.ForeignKey(User, related_name='test_submit_user_id')
    submit_time = models.DateTimeField(auto_now_add=True)
    submit = models.CharField(max_length=10)
    score = models.IntegerField(null=True)