# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-10 14:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_video_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='test_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]