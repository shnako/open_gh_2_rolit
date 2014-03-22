from django.conf.urls import patterns, url
import api

urlpatterns = patterns('',
    url(r'^set_light_bulb_intensity/$', api.set_light_bulb_intensity, name='set_light_bulb_intensity'),
    url(r'^get_light_bulb_intensity/$', api.get_light_bulb_intensity, name='get_light_bulb_intensity'),
    url(r'^get_temperature/$', api.get_temperature, name='get_temperature'),
    url(r'^get_power_usage/$', api.get_power_usage, name='get_power_usage')
)
