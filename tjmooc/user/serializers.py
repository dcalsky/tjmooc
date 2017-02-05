from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(min_length=6, max_length=20)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'nickname', 'password', 'avatar', 'last_login', 'date_joined')

    def create(self, validated_data):
        return super(UserRegistrationSerializer, self).create(validated_data)

    # def validate(self, attrs):
    #     # todo Password length limitation
    #     pass
        # if attrs.get('password') != attrs.get('confirm_password'):
        #     raise serializers.ValidationError("Those passwords don't match.")
        # return attrs

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email', 'nickname', 'avatar', 'last_login', 'date_joined')
#         write_only_fields = ('password',)


class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source='key')

    class Meta:
        model = Token
        fields = ("auth_token",)
