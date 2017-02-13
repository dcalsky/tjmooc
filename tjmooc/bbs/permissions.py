from rest_framework import permissions
from django.conf import settings

secret = settings.SECRET_KEY

class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.id == obj.owner.id


class IsTeacherOrManager(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name__in=['teacher', 'manager']).exists()