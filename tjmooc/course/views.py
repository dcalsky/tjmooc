from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import request
from .permissions import IsObligatorOrManagerReadOnly, IsStudent
from .serializers import CourseSerializer, ChapterSerializer, CourseParticipationSerializer, UnitSerializer, VideoSerializer
from .models import Course, Chapter, CourseParticipation, Video, Unit


class ResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page'
    max_page_size = 1000


class CourseList(ListAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = ResultsSetPagination



class CourseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'id'


class ChapterList(ListAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ChapterDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()
    lookup_field = 'id'

class UnitList(ListAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()


class UnitDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
    lookup_field = 'id'


class VideoList(ListAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


class VideoDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    lookup_field = 'id'


