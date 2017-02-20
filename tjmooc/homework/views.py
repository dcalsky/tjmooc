from django.shortcuts import render
from django.http import Http404
from rest_framework import status, generics
from rest_framework.response import Response
from .models import Homework, HomeworkSubmit, Test, TestSubmit
from .serializer import HomeworkSerializer, HomeworkSubmitSerializer, TestSerializer, TestSubmitSerializer
from rest_framework.views import APIView
from .permissions import IsTeacherOrManagerOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class HomeworkList(generics.ListCreateAPIView):
    permission_classes = (IsTeacherOrManagerOrReadOnly, )
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class HomeworkDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTeacherOrManagerOrReadOnly, )
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    lookup_field = 'id'



class HomeworkSubmitList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = HomeworkSubmit.objects.all()
    serializer_class = HomeworkSubmitSerializer


class HomeworkSubmitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = HomeworkSubmit.objects.all()
    serializer_class = HomeworkSubmitSerializer
    lookup_field = 'id'


class TestList(generics.ListCreateAPIView):
    permission_classes = (IsTeacherOrManagerOrReadOnly,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsTeacherOrManagerOrReadOnly,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    lookup_field = 'id'


class TestSubmitList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = TestSubmit.objects.all()
    serializer_class = TestSubmitSerializer


class TestSubmitDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = TestSubmit.objects.all()
    serializer_class = TestSubmitSerializer
    lookup_field = 'id'




