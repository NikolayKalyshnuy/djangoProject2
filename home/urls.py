from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),
    re_path(r'^api/\d+$', views.re_home)
]
