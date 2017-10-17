from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'email']


admin.site.register(User, AccountAdmin)
