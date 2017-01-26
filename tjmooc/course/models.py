from django.db import models


class Course(models.Model):
    title = models.TextField(help_text='标题')
    subtitle = models.TextField(help_text='副标题')
    introduction = models.TextField(help_text='内容介绍')
    cover_image = models.ImageField(help_text='封面图')
    sections = models.TextField(default='', help_text='章')  # store a string for (de)serialization
    update_time = models.DateTimeField(auto_now_add=True, help_text='更新时间')
    participants_count = models.IntegerField(default=0, help_text='参与人数')
    # 负责老师ID


class Chapter(models.Model):
    units = models.TextField(help_text='单元')
    title = models.TextField(help_text='标题')
    description = models.TextField(help_text='说明')
    materials = models.TextField(help_text='课程资料')


class Unit(models.Model):
    title = models.TextField(help_text='标题')
    description = models.TextField(help_text='说明')
    lists = models.TextField(help_text='内容')


class Video(models.Model):
    title = models.TextField(help_text='标题')
    description = models.TextField(help_text='说明')
    upload_time = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    url = models.URLField(help_text='链接')
    # 授课老师ID


class CourseParticipation(models.Model):
    # 参与者ID
    course_id = models.ForeignKey(Course, help_text='课程ID')
    finished = models.BooleanField(default=False, help_text='是否完成')
    time = models.DateTimeField(auto_now_add=True)
    total_score = models.IntegerField(default=0, help_text='作业与测试的总分')
