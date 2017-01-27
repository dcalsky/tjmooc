from django.contrib import admin
from .models import Homework, HomeworkSubmit, Test, TestSubmit
admin.site.register(Homework, HomeworkSubmit, TestSubmit, Test)