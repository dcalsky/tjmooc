from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'course', CourseViewSet)
router.register(r'chapter', ChapterViewSet)
router.register(r'unit', UnitViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
