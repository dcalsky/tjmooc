from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class SessionSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'nickname', 'avatar', 'last_login', 'date_joined', 'groups', 'phone')
