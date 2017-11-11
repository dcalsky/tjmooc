from rest_framework import permissions
from django.conf import settings
from .models import *

secret = settings.SECRET_KEY


class IsObligatorOrLeactureOrManagerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.groups.filter(name__in=['manager']).exists():
            return True
        else:
            if 'obligator' in obj.__dir__():
                return request.user == obj.obligator
            elif 'leacturer' in obj.__dir__():
                return request.user == obj.leacturer


class IsManager(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            if isinstance(obj, Course):
                return request.user.id == obj.assistant.id or request.user.id == obj.lecturer.id


class IsOwner(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if isinstance(obj, TestSubmit) or isinstance(obj, HomeworkSubmit):
            return request.user.id == obj.user.id
