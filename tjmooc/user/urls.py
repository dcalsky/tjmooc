from django.conf.urls import url, include
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets
from .serializers import UserSerializer
from . import views

User = get_user_model()


class AccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^$', show, name='show'),
    url(r'$', views.UserViewList.as_view()),
    # url(r'^register$', new, name='register'),
    url(r'^api-auth$', include('rest_framework.urls', namespace='rest_framework'))
]
