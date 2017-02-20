from django.contrib import admin
from .models import Homework, HomeworkSubmit, Test, TestSubmit

admin.site.register(Homework)
admin.site.register(HomeworkSubmit)
admin.site.register(Test)
admin.site.register(TestSubmit)