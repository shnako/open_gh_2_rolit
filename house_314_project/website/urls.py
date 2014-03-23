__author__ = 'VladIulian'
from django.conf.urls import patterns, url
from website import views


urlpatterns = patterns('',
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^house/$', views.house, name='house'),
)