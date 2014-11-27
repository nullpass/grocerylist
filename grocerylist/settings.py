# grocerylist/settings.py
import os

from django.conf import global_settings

import cfggrocerylist

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
ROOT_URLCONF = 'grocerylist.urls'
WSGI_APPLICATION = 'grocerylist.wsgi.application'
FORCE_SCRIPT_NAME = cfggrocerylist.FORCE_SCRIPT_NAME

SECRET_KEY = cfggrocerylist.SECRET_KEY
SOCIAL_AUTH_TWITTER_KEY = cfggrocerylist.SOCIAL_AUTH_TWITTER_KEY
SOCIAL_AUTH_TWITTER_SECRET = cfggrocerylist.SOCIAL_AUTH_TWITTER_SECRET

DEBUG = cfggrocerylist.DEBUG
TEMPLATE_DEBUG = DEBUG
ALLOWED_HOSTS = cfggrocerylist.ALLOWED_HOSTS

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stores',
    'isles',
    'items',
    'lists',
    'social.apps.django_app.default',
    'recent',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.open_id.OpenIdAuth',
    'social.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
)

DATABASES = cfggrocerylist.DATABASES

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '_templates'),
    )

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
)
