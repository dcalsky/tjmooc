# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-31 11:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20171028_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='lists',
        ),
    ]