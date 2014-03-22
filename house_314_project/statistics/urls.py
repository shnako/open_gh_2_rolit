__author__ = 'VladIulian'
from django.conf.urls import patterns, url
from statistics import api

urlpatterns = patterns('',
    url(r'^get_current_consumption/$', api.get_current_consumption, name='get_current_consumption'),
    url(r'^get_average_consumption/$', api.get_average_consumption, name='get_average_consumption'),
    url(r'^get_area_average_consumption/$', api.get_area_average_consumption, name='get_area_average_consumption'),
    url(r'^get_city_average_consumption/$', api.get_city_average_consumption, name='get_city_average_consumption'),
)