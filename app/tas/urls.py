from django.conf.urls import patterns, url
from django.conf import settings


urlpatterns = patterns('',
    url(r'^$', 'tas.views.index'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^__test__$', 'tas.views.index'),
    )
