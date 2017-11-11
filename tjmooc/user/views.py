from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.generics import GenericAPIView, RetrieveUpdateAPIView
from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import *
from .permissions import IsOwnerOrReadOnly

User = get_user_model()


@api_view(['GET'])
@permission_classes((AllowAny,))
def check_user_name(request, username):
    if not User.objects.filter(username=username):
        return Response({
            'detail': 'ok'
        })
    else:
        return Response({
            'detail': 'existed'
        })


class UserRegistration(CreateModelMixin, GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserDetail(RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()
    lookup_field = 'username'

#
# class BecomeAssistant(APIView):
#     permission_classes = (AllowAny,)
#
#     def post(self, request):
#         user = User.objects.filter(id=request.data['user_id'])
#         assistant = Group.objects.get(name='assistant')
#         if not assistant:
#             return Response({
#                 'message': 'Assistant group is not exists!'
#             })
#
#         assistant.user_set.add(user)
#
#     def delete(self, request):
#         user = User.objects.filter(id=request.data['user_id'])
#         assistant = Group.objects.get(name='assistant')
#         if not assistant:
#             return Response({
#                 'message': 'Assistant group is not exists!'
#             })
#
#         assistant.user_set.remove(user)
