from django.conf.urls import url
from . import views
from django.conf.urls import include


urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
]
