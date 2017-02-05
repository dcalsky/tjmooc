from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import SessionSerializer
from user.serializers import UserRegistrationSerializer, TokenSerializer

User = get_user_model()

#
# class SessionViewList(APIView):
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             serializer = UserRegistrationAPIView(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(status=status.HTTP_401_UNAUTHORIZED)
#
#     def delete(self, request):
#         pass


class UserLoginAPIView(GenericAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = SessionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.user
            token, _ = Token.objects.get_or_create(user=user)
            return Response(
                data=TokenSerializer(token).data,
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                data=serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )
