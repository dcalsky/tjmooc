from rest_framework import permissions
from django.conf import settings

secret = settings.SECRET_KEY


class IsObligatorOrLeactureOrManagerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.user.groups.filter(name__in=['manager']).exists():
            return True
        else:
            if 'obligator' in obj.dir():
                return request.user.id == obj.obligator.id
            elif 'leacturer' in obj.dir():
                return request.user.id == obj.leacture.id



class IsStudent(permissions.IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name__in=['student']).exists()