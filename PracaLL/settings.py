"""
Django settings for PracaLL project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'nzpdr3)8@ido_cx*7#4m^e2l0)&y9ej8zavix+wnna70u!knoi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'rest_framework',
    'logowanie',
    'pokoje',
    'rejestracja',
    'cpracownik',
    'apiRest',
 
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'PracaLL.urls'

WSGI_APPLICATION = 'PracaLL.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'pl'

TIME_ZONE = 'Europe/Warsaw'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/static/',
)

#Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = 'django.contrib.auth.views.login'

REST_FRAMEWORK = {
   
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}