from django.conf.urls import patterns, url
import api

urlpatterns = patterns('',
    url(r'^set_light_bulb_intensity/$', api.set_light_bulb_intensity, name='set_light_bulb_intensity'),
    url(r'^get_light_bulb_intensity/$', api.get_light_bulb_intensity, name='get_light_bulb_intensity'),
    url(r'^get_temperature/$', api.get_temperature, name='get_temperature'),
    url(r'^get_current_consumption/$', api.get_current_consumption, name='get_current_consumption'),
)
