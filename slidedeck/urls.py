from django.urls import path, include, re_path
from django.contrib import admin
from django.http import HttpResponsePermanentRedirect
import slidedeck.settings as settings

import main.views

urlpatterns = [
    # main
    path(settings.URL_PREFIX + r'', main.views.index, name='index'),
    path(settings.URL_PREFIX + r'about/', main.views.about, name='about'),
    re_path(settings.URL_PREFIX + r'(MLSS-2012-.*)/', main.views.slides, name='slides'),

    # just for testing
    path(settings.URL_PREFIX + r'fake500/',  main.views.fake500,                      name='fake500'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # path(settings.URL_PREFIX + r'admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path(settings.URL_PREFIX + r'admin/', admin.site.urls),
]


#if settings.SERVE_STATIC:
#    urlpatterns += patterns('',
#        # Static serve for development
#        (settings.URL_PREFIX + r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
#    )


handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'
