# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-17 07:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0003_auto_20171015_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsubmit',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
