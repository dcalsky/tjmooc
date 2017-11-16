from rest_framework.serializers import *
from course.models import Course, Chapter, Unit
from material.serializers import *


class UnitSerializer(ModelSerializer):
    videos = VideoSerializer(source='video_set', many=True, read_only=True)

    class Meta:
        model = Unit
        fields = '__all__'


class ChapterSerializer(ModelSerializer):
    tests = TestSerializer(source='test_set', many=True, read_only=True)
    homeworks = HomeworkSerializer(source='homework_set', many=True, read_only=True)
    units = UnitSerializer(source='unit_set', many=True, read_only=True)

    class Meta:
        model = Chapter
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    chapters = ChapterSerializer(source='chapter_set', many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class UpdateAssistantSerializer(Serializer):
    user = PrimaryKeyRelatedField(queryset=User.objects.all())
    course = PrimaryKeyRelatedField(queryset=Course.objects.all())

    def update(self, instance, validated_data):
        instance.assistant = validated_data.get('user', instance.assistant)
        instance.save()
        return instance

