"""
Django settings for djangocon project.

Generated by 'django-admin startproject' using Django 1.9a1.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = os.getenv('DJANGO_DEBUG') != 'FALSE'

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'debug')


ALLOWED_HOSTS = [
    'djangocon.eu',
    'www.djangocon.eu',
    '2016.djangocon.eu',
    'djangocon-europe-2016.herokuapp.com',
]


DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///%s' % os.path.join(BASE_DIR, 'db.sqlite3')
    ),
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'bootstrapform',
    'django_activeurl',

    'cfp',
    'scholarships',
    'sponsors',
    'speakers',
    'djangocon.tplutils',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangocon.urls'


# Templates stuff
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

if not DEBUG:
    del TEMPLATES[0]['APP_DIRS']
    TEMPLATES[0]['OPTIONS']['loaders'] = [
        ('django.template.loaders.cached.Loader', [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ]),
    ]

WSGI_APPLICATION = 'djangocon.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
if not DEBUG:
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Budapest'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'public')
STATIC_URL = '/static/'
if not DEBUG:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'


# Email stuff
ADMINS = (('DjangoCon Team', '2016@djangocon.eu'),)
SERVER_EMAIL = '2016@djangocon.eu'
EMAIL_SUBJECT_PREFIX = '[2016.djangocon.eu] '


# Tinyblog stuff
TINYBLOG_ROOT_DIR = os.path.join(BASE_DIR, 'tinyblog', 'articles')


if DEBUG:
    # Use `python -m http.server 8888` from the uploads/ directory to serve
    MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
    MEDIA_URL = 'http://localhost:8888/'
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
else:
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    EMAIL_HOST = 'smtp.mandrillapp.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

    # Opbeat config
    INSTALLED_APPS += (
    'opbeat.contrib.django',
    )
    OPBEAT = {
        'ORGANIZATION_ID': '4fc5971f51514ef18b7fd9cde21a250b',
        'APP_ID': 'd5603a9e18',
        'SECRET_TOKEN': os.getenv('OPBEAT_SECRET_TOKEN'),
    }
    MIDDLEWARE_CLASSES = [
        'opbeat.contrib.django.middleware.OpbeatAPMMiddleware',
    ] + MIDDLEWARE_CLASSES
