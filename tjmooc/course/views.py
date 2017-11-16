from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.viewsets import *
from rest_framework.views import APIView, Response, status
from rest_framework.decorators import detail_route, list_route
from course.permissions import *
from course.serializers import *
from course.models import Course, Chapter, CourseParticipation, Unit
from django.http import Http404


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


class CourseViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    @list_route(methods=['get'])
    def top(self, request):
        courses = Course.objects.filter(top=True).order_by('-update_time')
        serializer = CourseSerializer(courses, data=[], many=True)
        if serializer.is_valid():
            return Response(serializer.data)
        return Response(serializer.errors)

    @detail_route(methods=['post', 'delete'])
    def assistant(self, request, pk):
        if request.method == 'POST':
            return self.add_assistant(request, pk)
        else:
            return self.remove_assistant(request, pk)

    def add_assistant(self, request, pk):
        course = self.get_object()
        serializer = UpdateAssistantSerializer(course, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': 'ok'
            })
        return Response(serializer.errors)

    def remove_assistant(self, request, pk):
        course = self.get_object()
        course.assistant = None
        course.save()

        return Response({
            'message': 'ok'
        })


class ChapterViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ChapterSerializer
    queryset = Chapter.objects.all()


class UnitViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UnitSerializer
    queryset = Unit.objects.all()


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
