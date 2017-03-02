# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 07:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('material', '0001_initial'),
        ('course', '0002_auto_20170302_1554'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testsubmit',
            name='submit_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_submit_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testsubmit',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Test'),
        ),
        migrations.AddField(
            model_name='test',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.Unit'),
        ),
        migrations.AddField(
            model_name='homeworksubmit',
            name='homework_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Homework'),
        ),
        migrations.AddField(
            model_name='homeworksubmit',
            name='judge_user_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='homework_judge_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homeworksubmit',
            name='submit_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homework_submit_user_id', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homework',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='homeworks', to='course.Chapter'),
        ),
    ]
