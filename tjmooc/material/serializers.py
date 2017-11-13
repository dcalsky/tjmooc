import json
from rest_framework.validators import UniqueTogetherValidator, UniqueValidator

from rest_framework import serializers
from .models import *


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
    questions = QuestionSerializer(source='question_set', read_only=True, many=True)
    test_submits = serializers.PrimaryKeyRelatedField(source='testsubmit_set', read_only=True, many=True)

    class Meta:
        model = Test
        fields = '__all__'


class UserSerializerLite(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    nickname = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'nickname']


class HomeworkSubmitDisplaySerializer(serializers.ModelSerializer):
    user = UserSerializerLite(read_only=True)

    class Meta:
        model = HomeworkSubmit
        fields = '__all__'


class HomeworkSubmitSerializer(serializers.ModelSerializer):

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


class HomeworkSerializer(serializers.ModelSerializer):
    homework_submits = HomeworkSubmitSerializer(source='homeworksubmit_set', read_only=True, many=True)

    class Meta:
        model = Homework
        fields = '__all__'
