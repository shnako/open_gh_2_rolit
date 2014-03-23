__author__ = 'VladIulian'
from django.conf.urls import patterns, url
from statistics import api

urlpatterns = patterns('',
    url(r'^get_current_consumption/$', api.get_current_consumption, name='get_current_consumption'),
)