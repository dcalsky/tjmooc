# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-22 14:44
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(validators=[django.core.validators.MaxLengthValidator(50, '标题字数不能多于%(limit_value)s位!'), django.core.validators.MinLengthValidator(6, '标题字数不能少于%(limit_value)s位')])),
                ('content', models.TextField(error_messages={'blank': '帖子内容不能为空!'})),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbs.Forum')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='forum',
        ),
        migrations.RemoveField(
            model_name='post',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='floor',
            field=models.IntegerField(default=2),
        ),
        migrations.AddField(
            model_name='post',
            name='belong',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='bbs.Floor'),
            preserve_default=False,
        ),
    ]
