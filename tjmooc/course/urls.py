from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CourseList.as_view()),
    url(r'^(?P<cpk>\w+)$', views.CourseDetail.as_view()),
    url(r'^(?P<cpk>\w+)/attend$', views.CourseParticipationView.as_view()),
    url(r'^(?P<cpk>\w+)/chapter$', views.ChapterList.as_view()),
    url(r'^(?P<cpk>\w+)/chapter/(?P<pk>\w+)$', views.ChapterDetail.as_view()),
    url(r'^(?P<cpk>\w+)/chapter/(?P<pk>\w+)/unit$', views.UnitList.as_view()),
    url(r'^(?P<cpk>\w+)/chapter/(?P<pk>\w+)/unit/(?P<upk>\w+)$', views.UnitDetail.as_view())
]
