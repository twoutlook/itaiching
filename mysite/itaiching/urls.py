from django.conf.urls import url

from . import views

app_name = 'itaiching'
urlpatterns = [
    url(r'^$', views.style13, name='style13'),


]
