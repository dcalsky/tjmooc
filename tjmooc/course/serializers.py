from rest_framework.serializers import *
from course.models import Course, Chapter, Unit
from material.serializers import *


class AssistantSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'nickname']


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
    assistant = AssistantSerializer(read_only=True)

    class Meta:
        model = Course
        fields = '__all__'


class UpdateAssistantSerializer(Serializer):
    username = CharField(min_length=5)

    def validate_username(self, value):
        user = User.objects.filter(username=value).first()
        if user is None:
            raise ValidationError('This user is not exist!')
        return value

    def update(self, instance, validated_data):
        user = User.objects.filter(username=validated_data['username']).first()
        instance.assistant = user
        instance.save()
        return instance
