from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'test', TestViewSet)
router.register(r'test-submit', TestSumitViewSet)
router.register(r'homework', HomeworkViewSet)
router.register(r'homework-submit', HomeworkSubmitViewSet)
router.register(r'question', QuestionViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^video$', VideoListView.as_view()),
    url(r'^video/(?P<id>\d+)$', VideoDetailView.as_view()),
    url(r'^upload/', upload),
    url(r'^submits/(?P<id>\d+$)', BothSumbitViewSet.as_view())

]
