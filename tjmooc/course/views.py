from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView, Response, status
from .permissions import IsObligatorOrLeactureOrManagerOrReadOnly, IsStudent
from .serializers import CourseSerializer, ChapterSerializer, CourseParticipationSerializer, UnitSerializer
from .models import Course, Chapter, CourseParticipation, Unit
from django.http import Http404
import json


def get_course(course_id):
    try:
        return Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        raise Http404


def get_chapter_and_course(chapter_id, course_id):
    try:
        chapter = Chapter.objects.get(id=chapter_id)
    except Chapter.DoesNotExist:
        raise Http404
    course = get_course(course_id)
    if chapter_id not in course.sections:
        raise Http404
    return chapter, course


def get_unit_and_chapter_and_course(unit_id, chapter_id, course_id):
    try:
        unit = Unit.objects.get(id=unit_id)
    except Unit.DoesNotExist:
        raise Http404
    chapter, _ = get_chapter_and_course(chapter_id, course_id)
    if unit_id not in chapter.units:
        raise Http404
    return unit


class ResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page'
    max_page_size = 1000


class CourseList(ListCreateAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = ResultsSetPagination


class CourseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get(self, request, cpk):
        course = get_course(cpk)
        return Response(CourseSerializer(course).data,
                        status=status.HTTP_200_OK)

    def put(self, request, cpk):
        course = get_course(cpk)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class ChapterList(ListCreateAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

    def get(self, request, cpk):
        course_id = cpk
        course = get_course(course_id)
        chapters = course.sections
        objects = Chapter.objects.filter(id__in=chapters)
        serializer = ChapterSerializer(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        course_id = kwargs['cpk']
        course = get_course(course_id)

        serializer = ChapterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            chapters = course.sections
            chapters.append(serializer.data['id'])
            course.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ChapterDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

    def get(self, request, cpk, pk):
        course_id = cpk
        chapter_id = pk
        chapter, _ = get_chapter_and_course(chapter_id, course_id)
        return Response(ChapterSerializer(chapter), status=status.HTTP_200_OK)

    def put(self, request, cpk, pk):
        course_id = cpk
        chapter_id = pk

        chapter, _ = get_chapter_and_course(chapter_id, course_id)

        serializer = ChapterSerializer(chapter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


class UnitList(ListCreateAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def get(self, request, cpk, pk):
        course_id = cpk
        chapter_id = pk

        chapter, _ = get_chapter_and_course(chapter_id, course_id)
        objects = Unit.objects.filter(id__in=chapter.units)
        serializer = UnitSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, cpk, pk):
        course_id = cpk
        chapter_id = pk

        chapter, _ = get_chapter_and_course(chapter_id, course_id)
        serializer = UnitSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            units = chapter.units
            units.append(serializer.data['id'])
            chapter.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class UnitDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def get(self, request, cpk, pk, upk):
        course_id = cpk
        chapter_id = pk
        unit_id = upk

        unit, _, _ = get_unit_and_chapter_and_course(unit_id, chapter_id, course_id)

        return Response(UnitSerializer(unit), status=status.HTTP_200_OK)

    def put(self, request, cpk, pk, upk):
        course_id = cpk
        chapter_id = pk
        unit_id = upk

        unit, _, _ = get_unit_and_chapter_and_course(unit_id, chapter_id, course_id)

        serializer = ChapterSerializer(unit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)




class CourseParticipationView(APIView):
    permission_classes = (IsStudent, )

    def get(self, request, cpk):
        course = get_course(cpk)
        student = request.user

        participation = CourseParticipation.objects.filter(course_id=course, participant=student)
        if participation.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            course.participants_count += 1
            course.save()

            participation = CourseParticipation(participant=student, course_id=course)
            participation.save()

            participation_serializer = CourseParticipationSerializer(participation)
            return Response(participation_serializer.data, status=status.HTTP_200_OK)












