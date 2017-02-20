from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView, Response, status
from .permissions import IsObligatorOrManagerReadOnly, IsStudent
from .serializers import CourseSerializer, ChapterSerializer, CourseParticipationSerializer, UnitSerializer, VideoSerializer
from .models import Course, Chapter, CourseParticipation, Video, Unit
from django.http import Http404
import json


def get_course(course_id):
    try:
        return Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        raise Http404

def get_chapter(chapter_id):
    try:
        return Chapter.objects.get(id=chapter_id)
    except Chapter.DoesNotExist:
        raise Http404

def get_unit(unit_id):
    try:
        return Unit.objects.get(id=unit_id)
    except Unit.DoesNotExist:
        raise Http404



class ResultsSetPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page'
    max_page_size = 1000


class CourseList(ListCreateAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = ResultsSetPagination



class CourseDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


    def get(self, request, cpk):
        return Response(CourseSerializer(get_course(cpk)).data,
                        status=status.HTTP_200_OK)

    def put(self, request, cpk):
        course = Course.objects.get(id=cpk)
        serializer = CourseSerializer(course,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



class ChapterList(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

    def get(self, request, *args, **kwargs):
        course_id = kwargs['cpk']
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
    permission_classes = (IsAuthenticated, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()

    def get(self, request, *args, **kwargs):
        course_id = kwargs['cpk']
        chapter_id = kwargs['pk']

        course = get_course(course_id)

        if chapter_id not in course.sections:
            return Response(status=status.HTTP_404_NOT_FOUND)
        chapter = get_chapter(chapter_id)
        return Response(ChapterSerializer(chapter), status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        course_id = kwargs['cpk']
        chapter_id = kwargs['pk']
        course = get_course(course_id)

        if chapter_id not in course.sections:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ChapterSerializer(get_chapter(chapter_id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



class UnitList(ListCreateAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()








class UnitDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()
    lookup_field = 'pk'


# class VideoList(ListAPIView):
#     permission_classes = (IsObligatorOrManagerReadOnly, )
#     serializer_class = VideoSerializer
#     queryset = Video.objects.all()
#
#
# class VideoDetail(RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsObligatorOrManagerReadOnly, )
#     serializer_class = VideoSerializer
#     queryset = Video.objects.all()
#     lookup_field = 'id'


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

            partcipation_serializer = CourseParticipationSerializer(participation)
            return Response(partcipation_serializer.data, status=status.HTTP_200_OK)











            # if Course.objects.get(id=id) is None:
        #
        #     course_serializer = CourseSerializer(Course.objects.get(id=id))
        #     Response(course_serializer.data)
        # else:
        #     student = request.user
        #     course = Course.objects.get(id=id)











