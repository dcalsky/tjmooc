import json
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from rest_framework import serializers
from .models import *


class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class QuestionListSerializer(serializers.Serializer):
    questions = QuestionSerializer(many=True)

    def create(self, validated_data):
        questions = [Question(**item) for item in validated_data['questions']]
        return Question.objects.bulk_create(questions)

    def save(self):
        for question in self.validated_data['questions']:
            Question.objects.create(**question)


class TestSubmitSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        default=serializers.CurrentUserDefault()
    )
    answer = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = TestSubmit
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=TestSubmit.objects.all(),
                fields=('user', 'test'),
                message="请勿重复提交测试"
            )
        ]


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='get_questions', read_only=True, many=True)
    test_submits = TestSubmitSerializer(source='get_test_submits', read_only=True, many=True)

    class Meta:
        model = Test
        fields = '__all__'


class HomeworkSubmitSerializer(serializers.ModelSerializer):
    homework = serializers.PrimaryKeyRelatedField(queryset=Homework.objects.all())

    class Meta:
        model = HomeworkSubmit
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=HomeworkSubmit.objects.all(),
                fields=('user', 'homework'),
                message='请勿重复提交作业'
            )
        ]
