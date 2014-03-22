from django.conf.urls import patterns, include, url
import controls
import statistics

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'house_314_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^controls/', include('controls.urls')),
    url(r'^statistics/', include('statistics.urls')),
)
