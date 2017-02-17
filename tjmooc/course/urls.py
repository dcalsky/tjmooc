from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.CourseList.as_view()),
    url(r'^(?P<id>\w+)$', views.CourseDetail.as_view()),
    url(r'^chapter/$', views.ChapterList.as_view()),
    url(r'^chapter/(?P<id>\w+)$', views.ChapterDetail.as_view()),
    url(r'^chapter/unit$', views.UnitList.as_view()),
    url(r'^chapter/unit/(?P<id>\w+)$', views.UnitDetail.as_view())
]
