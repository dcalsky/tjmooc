import json
from rest_framework.validators import UniqueTogetherValidator

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

    def save(self):
        for question in self.validated_data['questions']:
            Question.objects.create(**question)


class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(source='get_questions', read_only=True, many=True)

    class Meta:
        model = Test
        fields = '__all__'


class TestSubmitSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    test = serializers.PrimaryKeyRelatedField(queryset=Test.objects.all())
    answer = serializers.ListField(child=serializers.CharField())

    def save(self):
        score = 0
        answer = self.validated_data['answer']
        print(answer)
        questions = Question.objects.filter(test_id=self.validated_data['test'])
        # Compare all answers of questions of user and teacher
        for i in range(questions.count()):
            question = questions[i]
            if i > len(answer) - 1:
                answer.append('')
            if question.right_answer == answer[i]:
                score = score + question.score
        TestSubmit.objects.create(score=score, **self.validated_data)

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


class HomeworkSubmitSerializer(serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    homework = serializers.PrimaryKeyRelatedField(queryset=Homework.objects.all())

    class Meta:
        model = HomeworkSubmit
        fields = '__all__'
