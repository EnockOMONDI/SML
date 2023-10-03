

"""
Django settings for academicstoday_project project.
Generated by 'django-admin startproject' using Django 1.8.
For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from pathlib import Path
import dj_database_url
from decouple import config
import sys
import cloudinary


# Import variables for our application. Basically all imported variables
# have a SECRET_* prefix.
try:
    from academicstoday_project.secret_settings import *
except ImportError:
    pass

# Import all constants to use throughout our application
try:
    from academicstoday_project.constants import *
except ImportError:
    pass

import django
from django.utils.encoding import force_str
django.utils.encoding.force_text = force_str

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_from_env = dj_database_url.config(conn_max_age=500)
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS= ['*']







# Application definition
#

INSTALLED_APPS = (
    'landpage',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'paypal.standard.ipn',
    'pyuploadcare.dj',
    'import_export',
    'ecommerce_app',
    'captcha',
    # 'jet',
    'account',
    'registration',
    'login',
    'registrar',
    'student',
    'teacher',
    'publisher',
    'cloudinary',
    'django.contrib.humanize',



   

  
    
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'academicstoday_project.urls'

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
                'ecommerce_app.context_processor.cart_item_count',

            ],
        },
    },
]

WSGI_APPLICATION = 'academicstoday_project.wsgi.application'


# Captcha App
#
if 'test' in sys.argv:
    CAPTCHA_TEST_MODE = True
CAPTCHA_FONT_SIZE = 52



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases




DATABASES = {
    'default': dj_database_url.config(
        default='postgres://brainlabske:2IXgxWya6kld@ep-proud-dream-08428657-pooler.us-east-2.aws.neon.tech/LMS'
    )
}






# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False



# Static files (CSS, JavaScript, Images) & Upload Content
# https://docs.djangoproject.com/en/1.7/howto/static-files/
# 'Sites Framework' requires this line.
# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

IMPORT_EXPORT_USE_TRANSACTIONS = True

SITE_ID = 1
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
   
)


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')



STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
    # Add to this list all the locations containing your static files 
)
