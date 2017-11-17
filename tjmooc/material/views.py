from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import *
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework.permissions import AllowAny, IsAuthenticated

from material.permissions import *
from material.serializers import *


class BothSumbitViewSet(APIView):
    def get(self, request, id):
        test_submits_queryset = TestSubmit.objects.filter(user=request.user, test__chapter_id=id)
        homework_submit_queryset = HomeworkSubmit.objects.filter(user=request.user, homework__chapter_id=id)
        test_submits_serialzier = TestSubmitSerializer(test_submits_queryset, many=True)
        homework_submits_serializer = HomeworkSubmitDisplaySerializer(homework_submit_queryset, many=True)

        return Response({
            'homework_submits': homework_submits_serializer.data,
            'test_submits': test_submits_serialzier.data
        })


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

    @detail_route(methods=['delete'])
    def clear_questions(self, request, pk=None):
        test = self.get_object()
        Question.objects.filter(test=test).delete()
        return Response({
            'message': 'ok'
        })


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

    @list_route(methods=['post'], url_path='list', serializer_class=QuestionListSerializer)
    def questions(self, request):
        serializer = QuestionListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class VideoViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = VideoSerializer
    queryset = Video.objects.all()


def upload(request):
    file_stroage = FileSystemStorage()
    if request.method == 'POST':
        file = request.FILES['file']

        file_stroage.save(file.name, file)
        return HttpResponse(file_stroage.url(file))
