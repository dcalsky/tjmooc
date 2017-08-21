from django.conf import settings
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from jwt import decode, DecodeError
from .permissions import IsOwnerOrReadOnly
from .models import Forum, Post
from .serializers import ForumSerializer, PostSerializer

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


class PostList(APIView):
    permission_classes = (AllowAny, )
    serializer_class = PostSerializer

    def post(self, request, format=None):
        data = request.data
        data['owner'] = request.user.id
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        return Post.objects.filter(forum_id=self.kwargs['forum_id'])


class PostDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    lookup_field = 'id'
