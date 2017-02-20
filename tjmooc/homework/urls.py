from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^homework/$', views.HomeworkList.as_view()),
	url(r'^homework/(?P<id>\w+)', views.HomeworkDetail.as_view()),
    url(r'^test/$', views.TestList.as_view()),
	url(r'^test/(?P<id>\w+)', views.TestDetail.as_view()),

]
