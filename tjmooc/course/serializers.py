from rest_framework.serializers import *
from course.models import Course, Chapter, Unit
from material.serializers import *


class UnitSerializer(ModelSerializer):
    class Meta:
        model = Unit
        fields = '__all__'


class ChapterSerializer(ModelSerializer):
    tests = TestSerializer(source='get_tests', many=True, read_only=True)
    homeworks = HomeworkSerializer(source='get_homeworks', many=True, read_only=True)
    units = UnitSerializer(source='get_units', many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    chapters = ChapterSerializer(source='get_chapters', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
