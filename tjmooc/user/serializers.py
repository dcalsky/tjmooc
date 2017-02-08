from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=4, max_length=16, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, min_length=6, max_length=20)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'nickname', 'password', 'avatar', 'last_login', 'date_joined')

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

