from pathlib import Path

from configurations import values


BASE_DIR = Path(__file__).resolve().parents[1]


class DjangoOverrides:
    """
    Overrides for built-in Django settings
    """

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.admindocs',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # Third-party
        # ...
    ]

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    ROOT_URLCONF = 'src.urls'

    TEMPLATES = [
        {
            'APP_DIRS': True,
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                BASE_DIR / 'src' / 'templates',
            ],
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
                'debug': values.BooleanValue(
                    False,
                    environ_name='DJANGO_DEBUG',
                    environ_prefix='',
                ),
            },
        },
    ]

    WSGI_APPLICATION = 'src.wsgi.application'

    USE_I18N = True
    USE_L10N = False
    USE_TZ = True
