from rest_framework import permissions
from django.conf import settings

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
            return request.user.id == obj.leacturer