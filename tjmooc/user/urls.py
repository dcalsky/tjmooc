from django.conf.urls import url
from .views import new, show

urlpatterns = [
    url(r'^$', show, name='show'),
    url(r'^registe$r', new, name='register')
]
