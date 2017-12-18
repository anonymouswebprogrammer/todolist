from django.conf.urls import url
from . import views
from django.conf.urls import include
from django.contrib import admin



urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
]
