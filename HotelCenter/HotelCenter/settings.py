"""
Django settings for HotelCenter project.
Generated by 'django-admin startproject' using Django 4.0.3.
For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import sys
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-hwa99f*i=q7)uxxkrpf(k$%2n%7jo4s4@rxiwnwzne7m76f#8_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

CORS_ORIGIN_WHITELIST = [
    'http://localhost',
    'http://localhost:3000'
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    'Account',
    'comment',
    'Hotel',
    'corsheaders',
    'Chat',
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'HotelCenter.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'HotelCenter.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'testdb.sqlite3',
    },

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'Hotel_center',
    #     'USER': 'root',
    #     'PASSWORD': 'my-secret-pw',
    #     'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
    #     'PORT': '3306',
    # },
    'TEST': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'testdb.sqlite3',
    }
}
# if 'test' in sys.argv:
#     DATABASES['default'] = DATABASES['TEST']

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    # 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     # 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

# URL used to access the media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, "media")

#
# # Default primary key field type
# # https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field
# STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
# STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))

# URL used to access the media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(STATIC_ROOT, "media")
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10 Mb limit

AUTH_USER_MODEL = 'Account.User'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',

}

# EMAIL
DOMAIN = 'localhost:3000'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "hotelcenter.noreply@gmail.com"
EMAIL_HOST_PASSWORD = "Vira1400SE1"
# DEFAULT_FROM_EMAIL = 'HotelCenter <no_reply@domain.com>'

DJOSER = {
    "SEND_ACTIVATION_EMAIL": True,
    # "SEND_CONFIRMATION_EMAIL": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "LOGOUT_ON_PASSWORD_CHANGE": True,
    'PASSWORD_RESET_CONFIRM_URL': 'reset-password/?uid={uid}&token={token}',  # Reset password Email

    'USERNAME_RESET_CONFIRM_URL': 'auth/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'auth/activate/{uid}/{token}',
    "EMAIL":
        {
            "activation": "Account.email.ActivationEmail",

        }
}

ASGI_APPLICATION = 'HotelCenter.asgi.application'

# Channels
ASGI_APPLICATION = 'HotelCenter.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# message broker for celery tasks
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
