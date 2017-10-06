from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import HomeworkListView, HomeworkDetailView, HomeworkSubmitListView, \
    HomeworkSubmitDetailView, TestListView, TestDetailView, TestSubmitListView, \
    TestSubmitDetailView, VideoListView, VideoDetailView, ProblemListView, ProblemDetailView, upload

urlpatterns = [
    url(r'^homework$', HomeworkListView.as_view()),
    url(r'^homework/(?P<id>\d+)$', HomeworkDetailView.as_view()),
    url(r'^homework/submit$', HomeworkSubmitListView.as_view()),
    url(r'^homework/(?P<id>\d+)/submit$', HomeworkSubmitListView.as_view()),
    url(r'^homework/(?P<hid>\d+)/submit/(?P<sid>\d+)$', HomeworkSubmitDetailView.as_view()),
    url(r'^test$', TestListView.as_view()),
    url(r'^test/(?P<id>\d+)$', TestDetailView.as_view()),
    url(r'^test/(?P<id>\d+)/submit$', TestSubmitListView.as_view()),
    url(r'^test/submit$', TestSubmitListView.as_view()),
    url(r'^test/(?P<tid>\d+)/submit/(?P<sid>\d+)$', TestSubmitDetailView.as_view()),
    url(r'^video$', VideoListView.as_view()),
    url(r'^video/(?P<id>\d+)$', VideoDetailView.as_view()),
    url(r'^problem$', ProblemListView.as_view()),
    url(r'^problem/<id>$', HomeworkListView.as_view()),
    url(r'^upload/', upload)

]
