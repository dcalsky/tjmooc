from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forums/$', views.ForumList.as_view()),
    url(r'^forums/(?P<forum_id>\w+)/floors/$', views.FloorList.as_view()),
    url(r'^floors/(?P<floor_id>\w+)/posts/$', views.PostList.as_view()),
    url(r'^floors/(?P<id>\w+)/$', views.FloorDetail.as_view())
]
