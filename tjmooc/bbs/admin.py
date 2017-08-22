from django.contrib import admin

from .models import Forum, Post, Floor


class ForumAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'owner']


class FloorAdmin(admin.ModelAdmin):
    list_display = ['title', 'forum', 'owner']


class PostAdmin(admin.ModelAdmin):
    list_display = ['belong', 'owner']


admin.site.register(Forum, ForumAdmin)
admin.site.register(Floor, FloorAdmin)
admin.site.register(Post, PostAdmin)
