from django.contrib import admin
from .models import Course, CourseParticipation, Chapter, Unit


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'participants_count', 'lecturer']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'course']


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'chapter']

