from rest_framework import permissions
from jwt import decode
from django.conf import settings

secret = settings.SECRET_KEY

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        token = request.auth
        if request.method in permissions.SAFE_METHODS:
            return True
        return decode(token, secret, algorithms=['HS256'])['username'] == obj.username