from django.db import models
from user.models import User
import jsonfield


class Course(models.Model):
    title = models.TextField(help_text='标题')
    subtitle = models.TextField(help_text='副标题')
    introduction = models.TextField(help_text='内容介绍')
    cover_image = models.TextField(help_text='封面图')
    sections = jsonfield.JSONField(help_text='章', default=list)  # store a string for (de)serialization
    update_time = models.DateTimeField(auto_now_add=True, help_text='更新时间')
    participants_count = models.IntegerField(default=0, help_text='参与人数')
    obligator = models.ForeignKey(User)
    top = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Chapter(models.Model):
    units = jsonfield.JSONField(help_text='单元', default=list)
    title = models.TextField(help_text='标题')
    description = models.TextField(help_text='说明')
    materials = jsonfield.JSONField(help_text='课程资料', default=list)
    leacturer = models.ForeignKey(User, null=False, blank=False)

    def __str__(self):
        return self.title


class Unit(models.Model):
    title = models.TextField(help_text='标题')
    description = models.TextField(help_text='说明')
    lists = jsonfield.JSONField(help_text='内容', default=list)
    leacturer = models.ForeignKey(User)

    def __str__(self):
        return self.title


class CourseParticipation(models.Model):
    participant = models.ForeignKey(User)
    course_id = models.ForeignKey(Course, help_text='课程ID')
    finished = models.BooleanField(default=False, help_text='是否完成')
    time = models.DateTimeField(auto_now_add=True)
    total_score = models.IntegerField(default=0, help_text='作业与测试的总分')

    def __str__(self):
        return self.participant.nickname + " " + self.course_id.title
