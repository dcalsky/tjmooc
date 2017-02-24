from functools import reduce
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import Response, status
from course.views import get_course, get_chapter_and_course, get_unit_and_chapter_and_course
from .serializer import HomeworkSerializer, HomeworkSubmitSerializer, TestSerializer, TestSubmitSerializer
from .models import Homework, HomeworkSubmit, Test, TestSubmit, Video
from course.models import Chapter, Course, Unit
from itertools import chain


def get_course_id_and_chapter_id(request):
    try:
        course_id = int(request.query_params.get('course'))
    except TypeError:
        course_id = None
    try:
        chapter_id = int(request.query_params.get('chapter'))
    except TypeError:
        chapter_id = None

    return course_id, chapter_id



class HomeworkListView(ListCreateAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()

    def get(self, request, *args, **kwargs):
        course_id, chapter_id = get_course_id_and_chapter_id(request)
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
        course_id, chapter_id = get_course_id_and_chapter_id(request)
        if course_id or chapter_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return self.create(request, *args, **kwargs)


class HomeworkDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = HomeworkSerializer
    queryset = Homework.objects.all()
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        course_id, chapter_id = get_course_id_and_chapter_id(request)
        if course_id is None or chapter_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        course_id, chapter_id = get_course_id_and_chapter_id(request)
        if course_id is None or chapter_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        course_id, chapter_id = get_course_id_and_chapter_id(request)
        if course_id is None or chapter_id is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            return self.destroy(request, *args, **kwargs)


class HomeworkSubmitListView(ListCreateAPIView):
    serializer_class = HomeworkSubmitSerializer
    queryset = HomeworkSubmit.objects.all()

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




















