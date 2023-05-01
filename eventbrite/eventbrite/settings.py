"""
Django settings for eventbrite project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from dotenv import load_dotenv
import os
from pathlib import Path
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m_6a@$+wqh_7d1skp^-#70+)7#glsdtie-3ypm9uw2d1^+dd03'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework.authtoken',
    'rest_framework',
    'event',
    'user',
    'booking',
    'drf_spectacular',
    'eventManagment',
    'sslserver',
    'storages',
    'corsheaders',
    'django_seed',
    'django_extensions',
    

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.security.SecurityMiddleware',
    # 'django_otp.middleware.OTPMiddleware',
    # 'two_factor.middleware.threadlocals.ThreadLocals',
    # 'two_factor.middleware.authy.AuthenticationStatusMiddleware',
    # 'django_otp.middleware.OTPMiddleware',
    # 'django.contrib.auth.middleware.AuthenticationMiddleware',
]


ROOT_URLCONF = 'eventbrite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'DIRS': [BASE_DIR / 'templates'],

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


WSGI_APPLICATION = 'eventbrite.wsgi.application'

#Glopal Database
# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DB_ENGINE'),
#         'NAME': os.getenv('DB_NAME'),
#         'ENFORCE_SCHEMA': os.getenv('DB_ENFORCE_SCHEMA'),
#         'CLIENT': {
#             'host': os.getenv('DB_CLIENT_HOST')
#         }
#     }
# }
# # Local Database
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
    }
}

# # Local Database
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DATABASE_ENGINE'),
        'NAME': os.environ.get('DATABASE_NAME'),
    }
}


# Password validation
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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')
TIME_ZONE = os.getenv('TIME_ZONE')
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# AUTH_USER_MODEL='eventbrit.User'
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
        'django.contrib.auth.backends.ModelBackend',  # default authentication backend
        'user.authentication.CustomTokenAuthentication'
    ],
    # 'DEFAULT_PERMISSION_CLASSES': [
    #     'rest_framework.permissions.IsAuthenticated',
    # ]

}

EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_PORT = os.getenv('EMAIL_PORT')


# EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS=True
# EMAIL_HOST='smtp.gmail.com'
# EMAIL_HOST_USER='eventus201@gmail.com'
# EMAIL_HOST_PASSWORD='adevsgoqzaixfobh'
# EMAIL_PORT=587
# Authentication settings
AUTH_USER_MODEL = os.getenv('AUTH_USER_MODEL')

# ALLOWED_HOSTS = ['52.55.220.111']
ALLOWED_HOSTS = ['*']

# Other settings ...

SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# SSL settings
SSL_CERTIFICATE = os.getenv('SSL_CERTIFICATE')
SSL_PRIVATE_KEY = os.getenv('SSL_PRIVATE_KEY')




PASSWORD_RESET_TIMEOUT_DAYS = 7

MEDIA_URL = '/'
MEDIA_ROOT = os.path.join(BASE_DIR, '')
CORS_ORIGIN_ALLOW_ALL = True



CELERY_BROKER_URL = 'mongodb://localhost:27017/eventbrite'
CELERY_RESULT_BACKEND = 'mongodb://localhost:27017/eventbrite'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERY_BEAT_SCHEDULE = {
    'update_event_status': {
        'task': 'eventbrite.celery.update_event_status',
        'schedule': 60 * 60 * 24, # run once per day
    },
}