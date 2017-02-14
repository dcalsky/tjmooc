from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    url(r'^$', obtain_jwt_token),
    # url(r'^$', views.UserLoginAPIView.as_view()),
]
