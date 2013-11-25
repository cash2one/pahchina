#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', '', name='index'),

    # url(r'^pahchina/', include('pahchina.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # include accounts
    url(r'^accounts/', include('pahchina.apps.accounts.urls')),
     url(r'^volunteer/', include('pahchina.apps.volunteer.urls')),
    url(r'^activity/', include('pahchina.apps.activity.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
