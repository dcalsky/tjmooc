from rest_framework import serializers
from .models import Homework, HomeworkSubmit, Test, TestSubmit

class HomeworkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Homework
        fields = ('title', 'introduction', 'problem_file', 'answer_file', 'deadline')

class HomeworkSubmitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HomeworkSubmit
        fields = ('homework_id', 'submit_user_id', 'judge_user_id',
                  'comment', 'score', 'submit_time', 'judge_time', 'submit_file')

class TestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Test
        fields = ('title', 'introduction', 'problem_file', 'answer_file', 'deadline')


class TestSubmitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TestSubmit
        fields = ('test_id', 'submit_user_id', 'submit_time', 'submit', 'score')



