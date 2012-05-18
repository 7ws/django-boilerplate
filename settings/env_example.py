'''
ATTENTION:
This is an example for environment-specific settings. Read the note on
settings/__init__.py to learn how to use this file and run the project.
'''

import sys

from settings import *  # Load main settings


MANAGERS = ADMINS = (
    (u'Developer Name', 'developer@email.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.' + (
            'sqlite3' if 'test' in sys.argv else 'postgresql_psycopg2'),
        'NAME': '',
    },
}

DEBUG = True

SITE_ID = 1

SECRET_KEY = 'PUT A SECRET CODE HERE'

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['127.0.0.1:11211']
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'ENABLED': True,
}
