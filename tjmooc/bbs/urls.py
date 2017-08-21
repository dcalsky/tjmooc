from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^forums/$', views.ForumList.as_view()),
    url(r'^forums/(?P<id>\w+)/$', views.ForumDetail.as_view()),
    url(r'^forums/(?P<forum_id>\w+)/posts/$', views.PostList.as_view()),
    url(r'^posts/(?P<id>\w+)/$', views.PostDetail.as_view())
]
