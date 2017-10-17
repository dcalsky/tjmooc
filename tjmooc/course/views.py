from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView, Response, status
from material.models import Video
from material.serializer import VideoSerializer
from course.permissions import IsObligatorOrLeactureOrManagerOrReadOnly, IsStudent
from course.serializers import CourseSerializer, ChapterSerializer, CourseParticipationSerializer, UnitSerializer
from course.models import Course, Chapter, CourseParticipation, Unit
from django.http import Http404, JsonResponse
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
    chapter, course = get_chapter_and_course(chapter_id, course_id)
    if unit_id not in chapter.units:
        raise Http404
    return unit, chapter, course


class ResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page'
    max_page_size = 1000


class CourseList(ListCreateAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = ResultsSetPagination

    def get(self, request, *args, **kwargs):

        if request.query_params.get('manage') is None:
            return super(CourseList, self).get(request, *args, **kwargs)
        else:
            u = request.user
            course = Course.objects.filter(obligator=request.user)
            return Response(CourseSerializer(course, many=True).data, status=status.HTTP_200_OK)

            # if course.exists():
            #     return Response(CourseSerializer(course, many=True).data, status=status.HTTP_200_OK)
            # else:
            #     return Response(status=status.HTTP_404_NOT_FOUND)


class CourseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    lookup_field = 'pk'

    def get(self, request, cpk):
        course = get_course(int(cpk))
        return Response(CourseSerializer(course).data,
                        status=status.HTTP_200_OK)

    def put(self, request, cpk):
        course = get_course(int(cpk))
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, *args, **kwargs):
        id = kwargs.get('cpk')
        self.kwargs['pk'] = id
        return super(CourseDetail, self).delete(request, *args, **kwargs)


class ChapterList(ListCreateAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

    def get(self, request, cpk):
        fileds_filter = [filed for filed in request.query_params]
        course_id = int(cpk)
        course = get_course(course_id)

        chapters = []
        for chapter_id in course.sections:
            chapters.append(Chapter.objects.get(id=chapter_id))
        serializer = ChapterSerializer(chapters, many=True, fields=fileds_filter)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        course_id = int(kwargs['cpk'])
        course = get_course(course_id)

        serializer = ChapterSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            chapters = course.sections
            chapters.append(serializer.data['id'])
            course.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class ChapterDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

    def get(self, request, cpk, pk):
        course_id = int(cpk)
        chapter_id = int(pk)
        chapter, _ = get_chapter_and_course(chapter_id, course_id)
        hw = list(chapter.homeworks.all())
        if len(hw) is not 0:
            hw = hw[0].id
            data = ChapterSerializer(chapter).data
            data['homework'] = hw
        else:
            data = ChapterSerializer(chapter).data
            data['homework'] = None

        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, cpk, pk):
        course_id = int(cpk)
        chapter_id = int(pk)

        chapter, _ = get_chapter_and_course(chapter_id, course_id)

        serializer = ChapterSerializer(chapter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, cpk, pk):
        course_id = int(cpk)
        chapter_id = int(pk)
        chapter, course = get_chapter_and_course(chapter_id, course_id)
        chapter.delete()
        course.sections.remove(chapter_id)
        course.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UnitList(ListCreateAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def get(self, request, cpk, pk):
        course_id = int(cpk)
        chapter_id = int(pk)
        chapter, _ = get_chapter_and_course(chapter_id, course_id)
        objects = Unit.objects.filter(id__in=chapter.units)
        serializer = UnitSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, cpk, pk):
        course_id = int(cpk)
        chapter_id = int(pk)

        chapter, _ = get_chapter_and_course(chapter_id, course_id)
        serializer = UnitSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            units = chapter.units
            units.append(serializer.data['id'])
            chapter.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class UnitDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrLeactureOrManagerOrReadOnly, )
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()

    def get(self, request, cpk, pk, upk):
        course_id = int(cpk)
        chapter_id = int(pk)
        unit_id = int(upk)

        unit, _, _ = get_unit_and_chapter_and_course(unit_id, chapter_id, course_id)

        return Response(UnitSerializer(unit).data, status=status.HTTP_200_OK)

    def put(self, request, cpk, pk, upk):
        course_id = int(cpk)
        chapter_id = int(pk)
        unit_id = int(upk)

        unit, _, _ = get_unit_and_chapter_and_course(unit_id, chapter_id, course_id)

        serializer = UnitSerializer(unit, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def delete(self, request, cpk, pk, upk):
        course_id = int(cpk)
        chapter_id = int(pk)
        unit_id = int(upk)

        unit, chapter, _ = get_unit_and_chapter_and_course(unit_id, chapter_id, course_id)
        chapter.units.remove(unit_id)
        unit.delete()
        chapter.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseParticipationView(APIView):
    permission_classes = (IsStudent, )

    def get(self, request, cpk):
        course = get_course(int(cpk))
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


class VideoView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Video.objects.all()
    serializer_class = VideoSerializer


    def get(self, request, cpk, pk, upk):
        try:
            unit = Unit.objects.get(id=int(upk))
        except Unit.objects.model.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            videos = Video.objects.filter(id__in=unit.lists)
            return Response(VideoSerializer(videos, many=True).data, status=status.HTTP_200_OK)

    def post(self, request, cpk, pk, upk):
        course_id = int(cpk)
        chapter_id = int(pk)
        unit_id = int(upk)
        unit, _, _ = get_unit_and_chapter_and_course(unit_id, chapter_id, course_id)

        serializer = VideoSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            unit.lists.append(serializer.data['id'])
            unit.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)


class TopView(APIView):
    permission_classes = (AllowAny, )
    def get(self, request):
        courses = Course.objects.filter(top=True).values()
        return JsonResponse({
            'result': json.dumps(courses)
        })