from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    url(r'^homework/', views.HomeworkList.as_view()),
	url(r'^homework/(?P<id>[0-9]+)/', views.HomeworkDetail.as_view()),
    url(r'^test/', views.TestkList.as_view()),
	url(r'^test/(?P<id>[0-9]+)/', views.TestkDetail.as_view()),

]
urlpatterns = format_suffix_patterns(urlpatterns)