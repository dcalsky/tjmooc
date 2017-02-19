from django.contrib import admin
from .models import Course, CourseParticipation, Chapter, Unit


admin.site.register(Course)
admin.site.register(Chapter)
admin.site.register(Unit)


# Register your models here.
