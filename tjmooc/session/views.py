from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import SessionSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework_jwt.settings import api_settings

User = get_user_model()

def jwt_response_payload_handler(token, user, request, *args, **kwargs):
    fields = ('id', 'username', 'email', 'nickname', 'avatar', 'last_login', 'date_joined', 'groups', 'phone')
    data = { 'token': token }
    for field in fields:
        data[field] = user.__dict__.get(field, '')
    return data

class DynamicFieldsModelSerializer(ModelSerializer):
    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class UserSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'nickname')


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }


class UserLoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SessionSerializer

    def post(self, request):
        serializer = SessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

        # def post(self, request, *args, **kwargs):
        #     serializer = self.get_serializer(data=request.data)
        #     if serializer.is_valid():
        #         user = serializer.user
        #         token, _ = Token.objects.get_or_create(user=user)
        #         return Response(
        #             data=TokenSerializer(token).data,
        #             status=status.HTTP_200_OK,
        #         )
        #     else:
        #         return Response(
        #             data=serializer.errors,
        #             status=status.HTTP_400_BAD_REQUEST,
        #         )
