from django.conf import settings
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from jwt import decode, DecodeError
from .permissions import IsOwnerOrReadOnly
from .models import Forum, Post, Floor
from .serializers import ForumSerializer, PostSerializer, FloorSerializer

secret = settings.SECRET_KEY


class ForumList(ListAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ForumSerializer
    queryset = Forum.objects.all()


class ForumDetail(RetrieveAPIView):
    permission_classes = (AllowAny, )
    serializer_class = ForumSerializer
    queryset = Forum.objects.all()
    lookup_field = 'id'


class FloorList(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = FloorSerializer
    queryset = Floor.objects.all()

    def post(self, request, format=None, **kwargs):
        data = request.data
        data['owner'] = request.user.id
        data['forum'] = self.kwargs['forum_id']
        serializer = FloorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Floor.objects.filter(forum_id=self.kwargs['forum_id'])


class PostList(ListCreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = PostSerializer

    def post(self, request, format=None, **kwargs):
        floor_id = self.kwargs['floor_id']
        floor = Floor.objects.get(id=floor_id)

        data = request.data
        data['owner'] = request.user.id
        data['belong'] = floor_id
        data['floor'] = floor.post_set.count() + 2

        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Post.objects.filter(belong_id=self.kwargs['floor_id'])


class FloorDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = FloorSerializer
    queryset = Floor.objects.all()
    lookup_field = 'id'
