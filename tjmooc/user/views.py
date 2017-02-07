from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView, ListCreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework import status
from django.core.exceptions import NON_FIELD_ERRORS
from .serializers import UserRegistrationSerializer

User = get_user_model()

@api_view(['GET'])
def check_user_name(request):
    if 'username' in request.query_params:
        username = request.query_params['username']
        if not User.objects.filter(username=username):
            return Response({
                'message': 'ok'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'message': 'error'
            })
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserList(ListCreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()


class UserRegistration(CreateModelMixin, GenericAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(RetrieveUpdateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

    # def get(self, request):
    #     user = User.objects.get(username=pk)
    #     serializer = UserRegistrationSerializer(user)
    #     return Response(data=serializer.data, status=status.HTTP_200_OK)



# class UserRegistrationAPIView(CreateAPIView):
#     authentication_classes = ()
#     permission_classes = ()
#     serializer_class = UserRegistrationSerializer
#
#     def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#
#         user = serializer.instance
#         token, created = Token.objects.get_or_create(user=user)
#         data = serializer.data
#         data["token"] = token.key
#
#         headers = self.get_success_headers(serializer.data)
#         return Response(data, status=status.HTTP_201_CREATED, headers=headers)
