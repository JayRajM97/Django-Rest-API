from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^Avengers/', views.HelloApiView.as_view()),
]
