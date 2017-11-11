from rest_framework import permissions
from django.conf import settings
from .models import *

secret = settings.SECRET_KEY


class IsTeacherOrManagerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.groups.filter(name__in=['teacher', 'manager']).exists()


class IsLeacturerOrManagerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if isinstance(obj, Video):
                return request.user == obj.teacher
            elif isinstance(obj, Test):
                return request.user == obj.unit.leacturer
            elif isinstance(obj, Homework):
                return request.user == obj.chapter.leacturer


class IsManager(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.groups.filter(name__in=['teacher', 'manager']).exists()


class IsOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, TestSubmit) or isinstance(obj, HomeworkSubmit):
            return request.user.id == obj.user.id
