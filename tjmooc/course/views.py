from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView, Response, status
from .permissions import IsObligatorOrManagerReadOnly, IsStudent
from .serializers import CourseSerializer, ChapterSerializer, CourseParticipationSerializer, UnitSerializer, VideoSerializer
from .models import Course, Chapter, CourseParticipation, Video, Unit
from django.http import Http404


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
    lookup_field = 'pk'


class ChapterList(ListAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class ChapterDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsObligatorOrManagerReadOnly, )
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()
    lookup_field = 'pk'

class UnitList(ListAPIView):
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

    def get_course(self, pk):
        try:
            Course.objects.get(id=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        course = self.get_course(pk)
        student = request.user


        participation = CourseParticipation.objects.get(course_id=course.id, participant=student.id)







        # if Course.objects.get(id=id) is None:
        #
        #     course_serializer = CourseSerializer(Course.objects.get(id=id))
        #     Response(course_serializer.data)
        # else:
        #     student = request.user
        #     course = Course.objects.get(id=id)











