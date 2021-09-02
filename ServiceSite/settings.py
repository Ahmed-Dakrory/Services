"""
Django settings for ServiceSite project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9q#6$z_ohh_$#&&^anu2d_26p3=&!641tm3+yij@e!#xy^l)-h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'sslserver',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mainApp',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ServiceSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mainApp.context_processor_file.defaultContextProcessor',
            ],
        },
    },
]

WSGI_APPLICATION = 'ServiceSite.wsgi.application'
# ASGI_APPLICATION = 'ServiceSite.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql', 
    'NAME': 'services',                      
    'USER': 'root',                      
    'PASSWORD': '',          
    'HOST': '127.0.0.1',                 
    'PORT': '3306',                      
        },
    }

# DATABASES = {
#     'default': {
#     'ENGINE': 'django.db.backends.mysql', 
#     'NAME': 'mhnatyco_main',                      
#     'USER': 'mhnatyco_ahmed',                      
#     'PASSWORD': 'A@123456789`134679',          
#     'HOST': '127.0.0.1',                 
#     'PORT': '3306',                      
#         },
#     }


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LOCALE_PATHS = (
   os.path.join(BASE_DIR, 'locale'),
)

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ar'

LANGUAGES = (
    ('ar', _('Arabic')),
    ('en', _('English')),
)

MULTILINGUAL_LANGUAGES = (
    "ar",
    "en",
)


TIME_ZONE = 'UTC'

USE_I18N = True


USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/mhnatyco/public_html/'#os.path.join(BASE_DIR, "static" , "static_root")

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

from pathlib import Path
home = str(Path.home())
print(home)
MEDIA_DIR = os.path.join(home,'media')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(home , 'media')
