from django.conf.urls import url
from .views import *
from material.views import VideoListView, VideoDetailView

urlpatterns = [
    url(r'^$', CourseList.as_view()),
    url(r'^(?P<cpk>\w+)$', CourseDetail.as_view()),
    url(r'^(?P<cpk>\w+)/attend$', CourseParticipationView.as_view()),
    url(r'^(?P<cpk>\w+)/chapter$', ChapterList.as_view()),
    url(r'^(?P<cpk>\w+)/chapter/(?P<pk>\w+)$', ChapterDetail.as_view()),
    url(r'^(?P<cpk>\w+)/chapter/(?P<pk>\w+)/unit$', UnitList.as_view()),
    url(r'^(?P<cpk>\w+)/chapter/(?P<pk>\w+)/unit/(?P<upk>\w+)$', UnitDetail.as_view()),
    url(r'^(?P<cpk>\w+)/chapter/(?P<pk>\w+)/unit/(?P<upk>\w+)/video$', VideoListView.as_view()),
    url(r'^top$', TopView.as_view())

]
