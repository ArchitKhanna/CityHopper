"""
Django settings for CityHopper project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l+z=7yqa#!b!%=!@+z2c77fld&0)i58ujn*8$0y-wolm!+nwh%'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
#id code
GOOGLE_ANALYTICS = {
    'google_analytics_id': 'UA-153486564-1',
}

# Application definition

INSTALLED_APPS = [
    'CityHopperApp.apps.CityhopperappConfig',
    'UsersApp.apps.UsersappConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #ERD Diagrams
    'django_spaghetti',
    #qr package
    'qr_code',
    #google_analytics package
    'google_analytics',
    'stripe',

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

ROOT_URLCONF = 'CityHopper.urls'
SETTINGS_PATH = os.path.dirname(os.path.dirname(__file__))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(SETTINGS_PATH, 'templates')],
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

WSGI_APPLICATION = 'CityHopper.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL='/media/'

LOGIN_REDIRECT_URL = 'cityhopper-home' # call your home page

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SPAGHETTI_SAUCE = {
  'apps':['auth','polls'],
  'show_fields':False,
  'exclude':{'auth':['user']},
  'show_proxy':True,
}

# Engine to activate session variables
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'

# cache for QR codes as are process intensive
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'qr-code': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'qr-code-cache',
        'TIMEOUT': 3600
    }
}

QR_CODE_CACHE_ALIAS = 'qr-code'


from qr_code.qrcode import constants
QR_CODE_URL_PROTECTION = {
    constants.TOKEN_LENGTH: 30,                         # Optional random token length for URL protection. Defaults to 20.
    constants.SIGNING_KEY: 'my-secret-signing-key',     # Optional signing key for URL token. Uses SECRET_KEY if not defined.
    constants.SIGNING_SALT: 'my-signing-salt',          # Optional signing salt for URL token.
    constants.ALLOWS_EXTERNAL_REQUESTS_FOR_REGISTERED_USER: True  # Tells whether a registered user can request the QR code URLs from outside a site that uses this app. It can be a boolean value used for any user or a callable that takes a user as parameter. Defaults to False (nobody can access the URL without the signature token).
}

#STRIPE KEYS WHICH ARE USED AS TOKENS
STRIPE_SECRET_KEY = 'sk_test_b7hFfuGB4WeY5ZyPTd4TOhfw005006UKF4'
STRIPE_PUBLISHABLE_KEY = 'pk_test_BcA2jJgEuGKNh5uEKvHsWXnS00Zpg7IQKS'


SPAGHETTI_SAUCE = {
  'apps':['auth','CityHopperApp'],
  'show_fields':False,
  'exclude':{'auth':['user']},
  'show_proxy':True,
}
