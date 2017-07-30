from django.contrib import admin
from .models import Homework, HomeworkSubmit, Test, TestSubmit, Video, Problem


class HomeworkAdmin(admin.ModelAdmin):
    list_display = ['title', 'introduction', 'deadline']


class HomeworkSubmitAdmin(admin.ModelAdmin):
    list_display = ['get_homework', 'get_user', 'score', 'submit_time']

    def get_homework(self, obj):
        return obj.homework_id.title

    def get_user(self, obj):
        return obj.submit_user_id.nickname


class TestAdmin(admin.ModelAdmin):
    list_display = ['title', 'deadline']


class TestSubmitAdmin(admin.ModelAdmin):
    list_display = ['get_test', 'get_user', 'score', 'submit_time']

    def get_test(self, obj):
        return obj.test.title

    def get_user(self, obj):
        return obj.submit_user.nickname

class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_user', 'upload_time']

    def get_user(self, obj):
        return obj.teacher.nickname




admin.site.register(Homework, HomeworkAdmin)
admin.site.register(HomeworkSubmit, HomeworkSubmitAdmin)
admin.site.register(Test, TestAdmin)
admin.site.register(TestSubmit, TestSubmitAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Problem)


# Register your models here.
