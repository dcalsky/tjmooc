# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-15 08:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homeworksubmit',
            name='update_time',
            field=models.TimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='testsubmit',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]