from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer

User = get_user_model()


class UserViewList(APIView):
    def get(self, request):
        if not request.query_params:
            return Response(status=status.HTTP_400_BAD_REQUEST)  # todo
        accounts = User.objects.filter(username=request.query_params['username'])
        users = UserSerializer(accounts, many=True)
        return Response(users.data)

    def post(self, request):
        user = UserSerializer(data=request.data)
        if user.is_valid():
            User.objects.create_user(
                username=request.data['username'],
                password=request.data['password']
            )
            return Response(user.data, status=status.HTTP_201_CREATED)
        else:
            return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)


def show(request):
    return render(request, 'user.show.html')


def new(request):
    return render(request, 'user.new.html')


def create(request):
    """
    Handle post request
    return Json
    """
    return JsonResponse()
