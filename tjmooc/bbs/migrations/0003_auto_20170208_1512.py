# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-08 07:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0002_auto_20170208_1512'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='course.Course'),
        ),
        migrations.AlterField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bbs.Post'),
        ),
    ]
