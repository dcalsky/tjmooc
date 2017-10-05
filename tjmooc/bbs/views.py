from django.conf import settings
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from .permissions import IsOwnerOrReadOnly
from .models import Forum, Post
from .serializers import ForumSerializer, PostSerializer

secret = settings.SECRET_KEY


class ForumList(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ForumSerializer
    queryset = Forum.objects.all()


class ForumDetail(RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ForumSerializer
    queryset = Forum.objects.all()
    lookup_field = 'id'


class PostList(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def list(self, request, *args, **kwargs):
        posts = self.paginate_queryset(self.get_queryset())
        serializer = PostSerializer(posts, many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        data['owner'] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
