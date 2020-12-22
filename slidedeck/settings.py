# Django settings for mlss12slides project.

import os

try:
    from .settings_local import *
except ImportError:
    raise Exception('Missing settings_local.py. Did you create it from the template?')

# Provide defaults if not imported from settings_local
DEBUG                      = locals().get('DEBUG', False)
DANGEROUS_ALL_IPS_INTERNAL = locals().get('DANGEROUS_ALL_IPS_INTERNAL', False)
EXTRA_TEMPLATE_DEBUG       = locals().get('EXTRA_TEMPLATE_DEBUG', False)
TEMPLATE_DEBUG             = locals().get('TEMPLATE_DEBUG', DEBUG or EXTRA_TEMPLATE_DEBUG)
CONTACT_EMAILS             = locals().get('CONTACT_EMAILS', ['jason.yosinski@gmail.com'])
SERVE_STATIC               = locals().get('SERVE_STATIC', False) # whether to enable static serve
ADMINS                     = locals().get('ADMINS', tuple())
MANAGERS                   = locals().get('MANAGERS', ADMINS)
URL_PREFIX                 = locals().get('URL_PREFIX', r'')
APPEND_SLASH               = locals().get('APPEND_SLASH', True)

ALLOWED_HOSTS = [SHORT_SITE_URL_BASE]

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'US/Eastern'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

MEDIA_ROOT         = BASE_DIR + '/media/'
STATIC_ROOT        = BASE_DIR + '/static/'
SITE_URL           = 'http://' + SHORT_SITE_URL
MEDIA_URL          = 'http://' + SHORT_SITE_URL + '/media/'
STATIC_URL         = 'http://' + SHORT_SITE_URL + '/static/'
SITE_URL_BASE      = 'http://' + SHORT_SITE_URL_BASE

if DANGEROUS_ALL_IPS_INTERNAL:
    # Make DEBUG available on all IPs
    from fnmatch import fnmatch
    class glob_list(list):
        def __contains__(self, key):
            for elt in self:
                if fnmatch(key, elt): return True
            return False

    INTERNAL_IPS = glob_list([
        '127.0.0.1',
        '*.*.*.*', # Use Debug carefully with this!
        ])

#TEMPLATE_DIRS = (
#    BASE_DIR + '/templates',
#)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True


ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

#MIDDLEWARE_CLASSES = (
#    'django.contrib.sessions.middleware.SessionMiddleware',
#    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
#    'django.contrib.auth.middleware.AuthenticationMiddleware',
#    'django.contrib.messages.middleware.MessageMiddleware',
#)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'slidedeck.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'main',
    'util',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]
#if DEBUG:
#    TEMPLATES[0]['OPTIONS']['string_if_invalid'] =  '{{ INVALID: %s }}'


# Extra template debug
if DEBUG and EXTRA_TEMPLATE_DEBUG:
    TEMPLATE_STRING_IF_INVALID = 'ERROR(%s)'

slideImgResolution  = 160
slideImgOrigSize    = 2000
slideImgThumbSize   = 200
slideImgThumbString = '.thumb'
