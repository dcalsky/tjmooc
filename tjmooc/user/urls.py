from django.conf.urls import url, include
from django.contrib.auth import get_user_model
from . import views

User = get_user_model()

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^$', show, name='show'),
    url(r'^$', views.UserRegistrationAPIView.as_view()),
    # url(r'^register$', new, name='register'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
