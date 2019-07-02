
from django.urls import re_path, path

from . import views

urlpatterns = [
    re_path(r'^$', views.home, name='home'),
    path('visitors/', views.visitors, name='visitors'),
]