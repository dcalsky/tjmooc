from django.contrib import admin
from .models import Course, CourseParticipation, Chapter, Unit


class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'participants_count', 'obligator']



class ChapterAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'leacturer']

class UnitAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'leacturer']

admin.site.register(Course, CourseAdmin)
admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Unit, UnitAdmin)
admin.site.register(CourseParticipation)


# Register your models here.
