from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.UserRegistration.as_view()),
    url(r'^(?P<username>\w+)$', views.UserDetail.as_view()),
    url(r'^(?P<username>\w+)/check$', views.check_user_name),
    # url(r'^assistant$', views.BecomeAssistant.as_view()),
]
