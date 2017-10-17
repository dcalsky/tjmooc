from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import *
from rest_framework.views import APIView
from rest_framework.response import Response

from course.models import Unit
from course.views import get_unit_and_chapter_and_course
from material.models import *
from material.permissions import IsTeacherOrManagerOrReadOnly, IsLeacturerOrManagerOrReadOnly
from rest_framework.permissions import AllowAny
from material.serializer import *


class HomeworkView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


class HomeworkDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer


# 作业的全部提交
class HomeworkSubmitView(ListCreateAPIView):
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    queryset = HomeworkSubmit.objects.all()
    serializer_class = HomeworkSubmitSerializer

    def list(self, request, id, **kwargs):
        serializer = HomeworkSubmitSerializer(HomeworkSubmit.objects.filter(homework_id=id), many=True)
        return Response(data=serializer.data)

    def create(self, request, id, **kwargs):
        data = request.data
        data['homework'] = id
        data['user'] = request.user.id
        serializer = HomeworkSubmitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestDetailView(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    permission_classes = (AllowAny,)
    queryset = Test.objects.all()
    serializer_class = TestSerializer


class TestSubmitView(APIView):
    def get(self, request, id):
        test = Test.objects.get(id=id)
        serializer = TestSubmitSerializer(test.testsubmit_set.all(), many=True)
        return Response(data=serializer.data)

    def post(self, request, id):
        data = request.data
        data['test'] = id
        data['user'] = request.user.id
        serializer = TestSubmitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionView(ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        if kwargs['id']:
            serializer = QuestionSerializer(data=Question.objects.filter(test_id=kwargs['id']), many=True)
        else:
            serializer = QuestionSerializer(data=Question.objects.all(), many=True)
        serializer.is_valid()
        return Response(data=serializer.data)


class QuestionListView(APIView):
    permission_classes = (AllowAny,)
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer

    def post(self, request):
        serializers = QuestionListSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status.HTTP_400_BAD_REQUEST)


def get_course_chapter_unit_id(request):
    pass


class VideoListView(ListCreateAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = (IsTeacherOrManagerOrReadOnly,)

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user')
        course_id, chapter_id, unit_id = get_course_chapter_unit_id(request)
        unit, _, _ = get_unit_and_chapter_and_course(unit_id, chapter_id, course_id)
        if unit_id is None:
            if user_id is None:
                return Response(status=status.HTTP_404_NOT_FOUND)
            else:
                videos = Video.objects.filter(teacher=user_id)
                serializer = VideoSerializer(videos, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            videos = Video.objects.filter(id__in=unit.lists)
            return Response(VideoSerializer(videos, many=True).data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        _, _, unit_id = get_course_chapter_unit_id(request)
        unit = Unit.objects.get(id=unit_id)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            video_id = serializer.data.get('id')
            unit.lists.append(video_id)
            unit.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class VideoDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = (IsLeacturerOrManagerOrReadOnly,)
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        video_id = int(kwargs.get('id'))
        _, _, unit_id = get_course_chapter_unit_id(request)
        unit = Unit.objects.get(id=unit_id)
        unit.lists.remove(video_id)
        unit.save()

        video = Video.objects.get(id=video_id)
        video.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def upload(request):
    file_stroage = FileSystemStorage()
    if request.method == 'POST':
        file = request.FILES['file']

        file_stroage.save(file.name, file)
        return HttpResponse(file_stroage.url(file))
