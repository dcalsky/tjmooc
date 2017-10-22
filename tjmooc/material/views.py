from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import AllowAny

from course.models import Unit
from course.views import get_unit_and_chapter_and_course
from material.models import *
from material.permissions import IsTeacherOrManagerOrReadOnly, IsLeacturerOrManagerOrReadOnly
from material.serializers import *


class HomeworkViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()


class HomeworkSubmitViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = HomeworkSubmitSerializer
    queryset = HomeworkSubmit.objects.all()


class TestViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TestSerializer
    queryset = Test.objects.all()


class TestSumitViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = TestSubmitSerializer
    queryset = TestSubmit.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = TestSubmitSerializer(data=request.data, context={
            'request': request
        })
        if serializer.is_valid():
            answer = serializer.validated_data['answer']
            score = 0
            questions = Question.objects.filter(test=serializer.validated_data['test'])
            for i in range(questions.count()):
                question = questions[i]
                if i > len(answer) - 1:
                    answer.append('')
                if question.right_answer == answer[i]:
                    score = score + question.score
            serializer.save(score=score)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class QuestionViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

    @list_route(methods=['post'], url_path='list')
    def questions(self, request):
        serializer = QuestionListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


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
