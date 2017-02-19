from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CourseList.as_view()),
    url(r'^(?P<pk>\w+)$', views.CourseDetail.as_view()),
    url(r'^(?P<pk>\w+)/attend$', views.CourseDetail.as_view()),
    url(r'^chapter/$', views.ChapterList.as_view()),
    url(r'^chapter/(?P<pk>\w+)$', views.ChapterDetail.as_view()),
    url(r'^chapter/unit$', views.UnitList.as_view()),
    url(r'^chapter/unit/(?P<pk>\w+)$', views.UnitDetail.as_view())
]
