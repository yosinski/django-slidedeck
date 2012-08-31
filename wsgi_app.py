# wsgi_app.py
# JBY: modified from http://www.westphahl.net/blog/2010/4/8/running-django-nginx-and-uwsgi/

import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi

print
print sys.path
print

application = django.core.handlers.wsgi.WSGIHandler()
