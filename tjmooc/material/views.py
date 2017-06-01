from functools import reduce
from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Response, status, APIView
from course.views import get_course, get_chapter_and_course,\
    get_unit_and_chapter_and_course
from .serializer import HomeworkSerializer, HomeworkSubmitSerializer, \
    TestSerializer, TestSubmitSerializer, VideoSerializer, ProblemSerializer
from .models import Homework, HomeworkSubmit, Test, TestSubmit, Video, Problem
from course.models import Chapter, Course, Unit
from django.http import Http404
from .permissions import IsLeacturerOrManagerOrReadOnly, IsTeacherOrManagerOrReadOnly


TESTSCORE = 100

def get_course_chapter_unit_id(request):
    try:
        course_id = int(request.query_params.get('course'))
    except TypeError:
        course_id = None
    try:
        chapter_id = int(request.query_params.get('chapter'))
    except TypeError:
        chapter_id = None
    try:
        unit_id = int(request.query_params.get('unit'))
    except TypeError:
        unit_id = None

    return course_id, chapter_id, unit_id


class HomeworkListView(ListCreateAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = (IsTeacherOrManagerOrReadOnly, )

    def get(self, request, *args, **kwargs):
        course_id, chapter_id, _ = get_course_chapter_unit_id(request)
        if course_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        elif chapter_id is not None:
            homeworks = Homework.objects.filter(chapter_id=chapter_id)
            serializer = HomeworkSerializer(homeworks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            course = get_course(course_id)
            homeworks = Homework.objects.filter(chapter__in=course.sections)
            serializer = HomeworkSerializer(homeworks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        course_id, chapter_id, _ = get_course_chapter_unit_id(request)
        if course_id or chapter_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return self.create(request, *args, **kwargs)


class HomeworkDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    permission_classes = (IsLeacturerOrManagerOrReadOnly, )
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        course_id, chapter_id, _ = get_course_chapter_unit_id(request)
        if course_id is None or chapter_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        course_id, chapter_id, _ = get_course_chapter_unit_id(request)
        if course_id is None or chapter_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        course_id, chapter_id, _ = get_course_chapter_unit_id(request)
        if course_id is None or chapter_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return self.destroy(request, *args, **kwargs)


class HomeworkSubmitListView(ListCreateAPIView):
    serializer_class = HomeworkSubmitSerializer
    queryset = HomeworkSubmit.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        user_id = request.query_params.get('user')
        if id is None:
            if user_id is None:
                Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                submits = HomeworkSubmit.objects.filter(submit_user_id=user_id)
                serializer = HomeworkSubmitSerializer(submits, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if user_id is None:
                submits = HomeworkSubmit.objects.filter(homework_id=id)
                serializer = HomeworkSubmitSerializer(submits, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                submits = HomeworkSubmit.objects.filter(homework_id=id,
                                                        submit_user_id=user_id)
                serializer = HomeworkSubmitSerializer(submits, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = HomeworkSubmitSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class HomeworkSubmitDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = HomeworkSubmitSerializer
    queryset = HomeworkSubmit
    permission_classes = (IsAuthenticatedOrReadOnly, )


    def check_homework_exist(self, request, *args, **kwargs):
        homework_id = kwargs.get('hid')
        submit_id = kwargs.get('sid')
        submit = HomeworkSubmit.objects.get(id=submit_id)
        return str(submit.homework_id_id) != homework_id, submit

    def get(self, request, *args, **kwargs):
        flag, submit = self.check_homework_exist(request, *args, **kwargs)
        if flag:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = HomeworkSubmitSerializer(submit)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        flag, submit = self.check_homework_exist(request, *args, **kwargs)
        if flag:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = HomeworkSubmitSerializer(submit, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        flag, submit = self.check_homework_exist(request, *args, **kwargs)
        if flag:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            submit.delete()


class TestListView(ListCreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsTeacherOrManagerOrReadOnly, )

    def get(self, request, *args, **kwargs):
        course_id, chapter_id, unit_id = get_course_chapter_unit_id(request)
        tests = Test.objects.filter(unit=unit_id)
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        course_id, chapter_id, unit_id = get_course_chapter_unit_id(request)

        try:
            unit = Unit.objects.get(id=unit_id)
        except Unit.DoesNotExist:
            raise Http404

        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            test_id = serializer.data.get('id')
            unit.lists.append({"id": test_id, "type": "test"})
            unit.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class TestDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsLeacturerOrManagerOrReadOnly, )
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        test_id = kwargs.get('id')
        _, _, unit_id = get_course_chapter_unit_id(request)
        unit = Unit.objects.get(id=unit_id)
        unit.lists.remove({"id": test_id, "type": "test"})
        unit.save()

        test = Test.objects.get(id=test_id)
        test.delete()
        return Response(status.HTTP_202_ACCEPTED)


class TestSubmitListView(ListCreateAPIView):
    serializer_class = TestSerializer
    queryset = Test.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        user_id = request.query_params.get('user')
        if id is None:
            if user_id is None:
                Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                submits = Test.objects.filter(submit_user=user_id)
                serializer = TestSubmitSerializer(submits, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if user_id is None:
                submits = TestSubmit.objects.filter(test=id)
                serializer = TestSubmitSerializer(submits, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                submits = TestSubmit.objects.filter(test=id, submit_user=user_id)
                serializer = TestSubmitSerializer(submits, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        id = kwargs.get('id')
        if id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = TestSubmitSerializer(data=request.data)
            test = Test.objects.get(id=serializer.data.get('test'))
            if serializer.data.get('submit') == test.answer:
                serializer.data['score'] = TESTSCORE

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class TestSubmitDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = HomeworkSubmitSerializer
    queryset = HomeworkSubmit
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def check_test_exist(self, request, *args, **kwargs):
        test_id = kwargs.get('tid')
        submit_id = kwargs.get('sid')
        submit = TestSubmit.objects.get(id=submit_id)
        return str(submit.test_id) != test_id, submit

    def get(self, request, *args, **kwargs):
        flag, submit = self.check_test_exist(request, *args, **kwargs)
        if flag:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = TestSubmitSerializer(submit)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        flag, submit = self.check_test_exist(request, *args, **kwargs)
        if flag:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = TestSubmitSerializer(submit, data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        flag, submit = self.check_test_exist(request, *args, **kwargs)
        if flag:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            submit.delete()


class VideoListView(ListCreateAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = (IsTeacherOrManagerOrReadOnly, )

    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get('user')
        if user_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            videos = Video.objects.filter(teacher=user_id)
            serializer = VideoSerializer(videos, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        _, _, unit_id = get_course_chapter_unit_id(request)
        unit = Unit.objects.get(id=unit_id)
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            video_id = serializer.data.get('id')
            unit.lists.append({"id": video_id, "type": "video"})
            unit.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class VideoDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    permission_classes = (IsLeacturerOrManagerOrReadOnly, )
    lookup_field = 'id'

    def delete(self, request, *args, **kwargs):
        video_id = kwargs.get('id')
        _, _, unit_id = get_course_chapter_unit_id(request)
        unit = Unit.objects.get(id=unit_id)
        unit.lists.remove({"id": video_id, "type": "test"})
        unit.save()

        test = Test.objects.get(id=video_id)
        test.delete()
        return Response(status.HTTP_202_ACCEPTED)


class ProblemListView(ListCreateAPIView):
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )

class ProblemDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProblemSerializer
    queryset = Problem.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    lookup_field = 'id'
















