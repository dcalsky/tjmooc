from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer

User = get_user_model()


class UserRegistrationAPIView(CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        user = serializer.instance
        token, created = Token.objects.get_or_create(user=user)
        data = serializer.data
        data["token"] = token.key

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

# class UserViewList(APIView):
#     def get(self, request):
#         if not request.query_params:
#             return Response(status=status.HTTP_400_BAD_REQUEST)  # todo
#         accounts = User.objects.filter(username=request.query_params['username'])
#         users = UserSerializer(accounts, many=True)
#         return Response(users.data)
#
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             user = User.objects.create(
#                 username=request.data['username'],
#                 password=request.data['password']
#             )
#             user.save()  # todo mv them to serializer.py
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# def show(request):
#     return render(request, 'user.show.html')


def new(request):
    return render(request, 'user.new.html')


def create(request):
    """
    Handle post request
    return Json
    """
    return JsonResponse()
