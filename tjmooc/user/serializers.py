from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'nickname', 'avatar', 'last_login', 'date_joined')
        write_only_fields = ('password',)
