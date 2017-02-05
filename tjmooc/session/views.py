from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_jwt.views import verify_jwt_token
from rest_framework.response import Response
from rest_framework import status
from user.serializers import UserSerializer

User = get_user_model()


class SessionViewList(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    def delete(self, request):
        pass

