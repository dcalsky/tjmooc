from django.contrib import admin
from .models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('type', 'score', 'test')


@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline']


@admin.register(HomeworkSubmit)
class HomeworkSubmitAdmin(admin.ModelAdmin):
    list_display = ['get_homework', 'get_user', 'update_time']

    def get_homework(self, obj):
        return obj.homework.id

    def get_user(self, obj):
        return obj.user.id


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'deadline']


@admin.register(TestSubmit)
class TestSubmitAdmin(admin.ModelAdmin):
    list_display = ['test', 'user', 'score', 'update_time']


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_user', 'upload_time']

    def get_user(self, obj):
        return obj.teacher.nickname

