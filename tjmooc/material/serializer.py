from rest_framework import serializers
from tjmooc.homework.models import Homework, HomeworkSubmit, Test, TestSubmit

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = '__all__'

class HomeworkSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeworkSubmit
        fields = '__all__'

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


class TestSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestSubmit
        fields = '__all__'



