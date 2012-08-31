from django.conf.urls.defaults import *
from django.http import HttpResponsePermanentRedirect
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # main
    url(r'^$', 'main.views.index', name='index'),

    # just for testing
    url(r'^fake500/$',  'main.views.fake500',                      name='fake500'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)


if settings.SERVE_STATIC:
    urlpatterns += patterns('',
        # Static serve for development
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
