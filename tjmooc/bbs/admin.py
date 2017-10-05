from django.contrib import admin

from .models import Forum, Post


class ForumAdmin(admin.ModelAdmin):
    list_display = ['name', 'course', 'owner']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'forum', 'owner']


admin.site.register(Forum, ForumAdmin)
admin.site.register(Post, PostAdmin)
