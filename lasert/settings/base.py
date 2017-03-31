"""
Django settings for lasert project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from os.path import join, dirname, expanduser

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(dirname(dirname(__file__)), '..')
TEMPLATE_DIR = BASE_DIR + '/templates'
home = expanduser("~")
PROJECT = '/opt/bitnami/apps/django/django_projects/lasert'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=8!6=!r)+sg^7k4bem-r05xls_1heyd(ans-9ybd)19zjs3c$j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['107.180.106.251','lasertt.com','127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lasertApp',
    'captcha',
    'froala_editor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware'
]

ROOT_URLCONF = 'lasert.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'django.template.context_processors.i18n'
            ],
        },
    },
]

WSGI_APPLICATION = 'lasert.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

print STATIC_URL
print STATIC_ROOT

# LOGGING
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': PROJECT+'/lasertt.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'lasertApp': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#         },
#     }
# }

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# Dynamic directory created
# if not os.path.exists(home+'/proflag'):
#     os.makedirs(home+'/proflag')

MEDIA_URL = '/media/'


IMG_RECOMMEND= 'recommend/'
IMG_CLIENTS='clients/'
IMG_PARTNERS='partners/'
IMG_SERVICE = 'service/'
FROALA_UPLOAD_PATH = 'froala/'
IMG_SLIDER = 'sliders/'


RECAPTCHA_PUBLIC_KEY = '6LdSQBoUAAAAAJAgz8lQJK-tFevaHjfyX_shnBti'
RECAPTCHA_PRIVATE_KEY = '6LdSQBoUAAAAAE3dX0wLwI3lVKHTypZQgx8_maaY'


SESSION_EXPIRE_AT_BROWSER_CLOSE = True

GRAPPELLI_ADMIN_TITLE = 'Lasert Admin Panel'


EMAIL_HOST = "mail.lasertt.com"
EMAIL_PORT = 25
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = 'no-replay@lasertt.com'
EMAIL_HOST_USER = 'no-replay@lasertt.com'
EMAIL_HOST_PASSWORD = 'mBa5bgM8}o7~'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


FROALA_EDITOR_PLUGINS = ('align', 'char_counter', 'code_beautifier' ,'code_view', 'colors', 'draggable', 'emoticons',
        'entities', 'file', 'font_family', 'font_size', 'fullscreen', 'image_manager', 'image', 'inline_style',
        'line_breaker', 'link', 'lists', 'paragraph_format', 'paragraph_style', 'quick_insert', 'quote', 'save', 'table',
        'url', 'video')
