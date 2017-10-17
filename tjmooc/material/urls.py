from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    url(r'^homework$', HomeworkView.as_view()),
    url(r'^homework/(?P<id>\d+)$', HomeworkDetailView.as_view()),
    url(r'^homework/(?P<id>\d+)/submit$', HomeworkSubmitView.as_view()),
    url(r'^test$', TestView.as_view()),
    url(r'^test/(?P<id>\d+)$', TestDetailView.as_view()),
    url(r'^test/(?P<id>\d+)/questions$', QuestionView.as_view()),
    url(r'^test/(?P<id>\d+)/submit$', TestSubmitView.as_view()),
    url(r'^video$', VideoListView.as_view()),
    url(r'^video/(?P<id>\d+)$', VideoDetailView.as_view()),
    url(r'^question$', QuestionView.as_view()),
    url(r'^questions$', QuestionListView.as_view()),
    url(r'^upload/', upload)

]
