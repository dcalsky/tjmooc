from rest_framework import permissions
from jwt import decode, DecodeError
from django.conf import settings

secret = settings.SECRET_KEY

class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        token = request.auth
        if request.method in permissions.SAFE_METHODS:
            return True
        try:
            jwt_username = decode(token, secret, algorithms=['HS256'])['username']
            return jwt_username == obj.username
        except DecodeError:
            return False