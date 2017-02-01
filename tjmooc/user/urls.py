from django.conf.urls import url, include
from .views import new, show
from rest_framework import routers, serializers, viewsets
from .models import Account
from .serializers import AccountSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

router = routers.DefaultRouter()
router.register(r'account', AccountViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^$', show, name='show'),
    url(r'^register$', new, name='register'),
    url(r'^api-auth$', include('rest_framework.urls', namespace='rest_framework'))
]
