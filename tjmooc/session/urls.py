from django.conf.urls import url, include
from . import views

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^$', show, name='show'),
    url(r'^$', views.SessionViewList.as_view()),
    # url(r'^register$', new, name='register'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
