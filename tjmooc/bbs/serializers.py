from rest_framework import serializers
from .models import Forum, Post
from course.models import Course
from django.contrib.auth import get_user_model


User = get_user_model()

class ForumSerializer(serializers.ModelSerializer):
    user_queryset = User.objects.all()
    course_queryset = Course.objects.all()
    name = serializers.CharField(min_length=3, max_length=20)
    owner = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=user_queryset)
    course = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=course_queryset) # required = True

    class Meta:
        model = Forum
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    forum_queryset = Forum.objects.all()
    post_queryset = Post.objects.all()
    title = serializers.CharField(min_length=6, max_length=50)
    content = serializers.CharField(error_messages={'blank': '帖子内容不能为空'})
    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    parent = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=post_queryset)

    class Meta:
        model = Post
        fields = '__all__'

