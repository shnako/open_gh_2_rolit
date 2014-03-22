from django.conf.urls import patterns, include, url
import house_314_raspberry_pi

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'house_raspi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/', include('house_314_raspberry_pi.urls')),
)
