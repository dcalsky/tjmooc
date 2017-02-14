# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 08:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import homework.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('introduction', models.TextField()),
                ('problem_file', models.FileField(upload_to=homework.models.homework_problem_path)),
                ('answer_file', models.FileField(upload_to=homework.models.homework_answer_path)),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HomeworkSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('score', models.IntegerField(null=True)),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('judge_time', models.DateTimeField(auto_now=True)),
                ('submit_file', models.FileField(upload_to=homework.models.homework_submit_path)),
                ('homework_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.Homework')),
                ('judge_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework_judge_user_id', to=settings.AUTH_USER_MODEL)),
                ('submit_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework_submit_user_id', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True)),
                ('introduction', models.TextField()),
                ('problem_file', models.FileField(upload_to=homework.models.homework_problem_path)),
                ('answer_file', models.FileField(upload_to=homework.models.homework_answer_path)),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TestSubmit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('submit', models.CharField(max_length=10)),
                ('score', models.IntegerField(null=True)),
                ('submit_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_submit_user_id', to=settings.AUTH_USER_MODEL)),
                ('test_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework.Test')),
            ],
        ),
    ]
