# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 03:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('units', models.TextField(help_text='单元')),
                ('title', models.TextField(help_text='标题')),
                ('description', models.TextField(help_text='说明')),
                ('materials', models.TextField(help_text='课程资料')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='标题')),
                ('subtitle', models.TextField(help_text='副标题')),
                ('introduction', models.TextField(help_text='内容介绍')),
                ('cover_image', models.ImageField(help_text='封面图', upload_to='')),
                ('sections', models.TextField(default='', help_text='章')),
                ('update_time', models.DateTimeField(auto_now_add=True, help_text='更新时间')),
                ('participants_count', models.IntegerField(default=0, help_text='参与人数')),
                ('obligator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='CourseParticipation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finished', models.BooleanField(default=False, help_text='是否完成')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('total_score', models.IntegerField(default=0, help_text='作业与测试的总分')),
                ('course_id', models.ForeignKey(help_text='课程ID', on_delete=django.db.models.deletion.CASCADE, to='course.Course')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='标题')),
                ('description', models.TextField(help_text='说明')),
                ('lists', models.TextField(help_text='内容')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(help_text='标题')),
                ('description', models.TextField(help_text='说明')),
                ('upload_time', models.DateTimeField(auto_now_add=True, help_text='创建时间')),
                ('url', models.URLField(help_text='链接')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
