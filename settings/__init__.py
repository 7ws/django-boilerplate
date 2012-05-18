'''
Main settings for the project.

ATTENTION:

These settings will not change across deploy environments. So, provide
the settings required to run this project on your environment in your
own local settings files, acording to the example included in the code
tree, "settings/env_example.py", and run the management commands using
the --settings option.

The environment-specific settings files will not be tracked by the
repository, according to the rules on .gitignore. The included example
must NOT be changed since it's part of the project. Instead, copy the
file using a name of your choice and tweak it according to your
environment.

Example:
% cp settings/env_example.py settings/my_settings.py
% ./manage.py runserver --settings=my_settings

Note: if you name your settings file "settings/default.py", you won't
need to provide the 'settings' option to management commands, as
'settings.default' is being expected out of the box.
'''

import os

from django.conf.global_settings import (
    TEMPLATE_CONTEXT_PROCESSORS, MIDDLEWARE_CLASSES,)
from django.core.urlresolvers import reverse_lazy


DEBUG = False
DEBUG_TOOLBAR_CONFIG = {
    'ENABLED': False
}

# Language
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Authentication urls
LOGIN_URL = reverse_lazy('user_login')
LOGOUT_URL = reverse_lazy('user_logout')
# LOGIN_REDIRECT_URL = reverse_lazy('...')

# Path/URL definitions
PROJECT_PATH = os.path.realpath(
    os.path.join(os.path.dirname(__file__), '..'))
PROJECT_ALIAS = os.path.basename(PROJECT_PATH)
ROOT_URLCONF = 'urls'

# User-uploaded files
MEDIA_ROOT = os.path.join(PROJECT_PATH, '_media')
MEDIA_URL = '/media/'

# Static files
STATIC_ROOT = os.path.join(PROJECT_PATH, '_static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)

# Templates
TEMPLATE_DEBUG = DEBUG
TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates'),
)
TEMPLATE_CONTEXT_PROCESSORS += (
    # ...
)

# Middlewares
MIDDLEWARE_CLASSES += (
    # ...
)

# Deploy
WSGI_APPLICATION = 'wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'gunicorn',

    # Local apps
    # ...
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
