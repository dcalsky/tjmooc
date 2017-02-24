from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HomeworkListView, HomeworkDetailView, HomeworkSubmitListView, HomeworkSubmitDetailView

urlpatterns = [
    url(r'^homework$', HomeworkListView.as_view()),
    url(r'^homework/(?P<id>\d+)$', HomeworkDetailView.as_view()),
    url(r'^homework/submit$', HomeworkSubmitListView.as_view()),
    url(r'^homework/(?P<id>\d+)/submit$', HomeworkSubmitListView.as_view()),
    url(r'^homework/(?P<hid>\d+)/submit/(?P<sid>\d+)$', HomeworkSubmitDetailView.as_view()),

]
