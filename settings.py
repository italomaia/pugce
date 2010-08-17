# -*- coding:utf-8 -*-

from os import path
try:
    import config
    config = config.config
except: 
    config = {"SECRET_KEY":"chave secreta"}

BIBLION_SECTIONS = []
BASE_DIR = path.abspath(path.dirname(__file__))
DEBUG = True
TEMPLATE_DEBUG = DEBUG

# WIKI PARAMS
# Defines the duration of the soft editing lock on article, in seconds.
WIKI_LOCK_DURATION = 15
# Determines if the wiki will be for registered users only, or 
# if it will allow anonimous users.
WIKI_REQUIRES_LOGIN = False

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': path.join(BASE_DIR, 'dev.sqlite'),                      # Or path to database file if using sqlite3.
            'USER': '',                      # Not used with sqlite3.
            'PASSWORD': '',                  # Not used with sqlite3.
            'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else: 
    DATABASES = {
        'default': {
            'ENGINE': config.DB_ENGINE,
            'NAME': config.DB_NAME,
            'USER': config.DB_USER,
            'PASSWORD': config.DB_PASSWD,
            'HOST': config.DB_HOST,
            'PORT': config.DB_PORT,
        }
    }

TIME_ZONE = 'America/Fortaleza'

LANGUAGE_CODE = 'pt-br'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = path.join(BASE_DIR, 'media_root')

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/admin_media/'

SECRET_KEY = config["SECRET_KEY"]

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pugce.urls'

TEMPLATE_DIRS = (
    path.join(BASE_DIR, 'templates'),
    path.join(BASE_DIR, 'biblion/templates'),
    path.join(BASE_DIR, 'wiki/templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages', 
    'django.contrib.admin',
    # -- APPS --
    'pugce.biblion',
    'pugce.wiki',
    'pugce.tagging',
)
