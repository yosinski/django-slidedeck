from django.conf.urls.defaults import *
from django.http import HttpResponsePermanentRedirect
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # main
    url(settings.URL_PREFIX + r'$', 'main.views.index', name='index'),
    url(settings.URL_PREFIX + r's/(.*)$', 'main.views.slides', name='slides'),

    # just for testing
    url(settings.URL_PREFIX + r'fake500/$',  'main.views.fake500',                      name='fake500'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    (settings.URL_PREFIX + r'admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (settings.URL_PREFIX + r'admin/', include(admin.site.urls)),
)


if settings.SERVE_STATIC:
    urlpatterns += patterns('',
        # Static serve for development
        (settings.URL_PREFIX + r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )


handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
