from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from . import views

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^$', show, name='show'),
    url(r'^$', obtain_jwt_token),
    # url(r'^register$', new, name='register'),
]
