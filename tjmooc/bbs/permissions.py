from rest_framework import permissions
from django.conf import settings

secret = settings.SECRET_KEY

class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    def has_object_permission(self, request, view, obj):
        token = request.auth
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.id == obj.owner.id
