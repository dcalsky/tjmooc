from django.contrib.auth import get_user_model
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import SessionSerializer
from user.serializers import UserRegistrationSerializer

User = get_user_model()


class UserLoginAPIView(GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SessionSerializer

    def post(self, request):
        serializer = SessionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

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
