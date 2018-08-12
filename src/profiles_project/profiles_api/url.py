from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name= 'hello-viewSet')
router.register('profile', views.UserProfileViewSet)
urlpatterns = [
    url(r'avengers', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
