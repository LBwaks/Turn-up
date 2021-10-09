"""
Django settings for TurnUp project.

Generated by 'django-admin startproject' using Django 3.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
from django.contrib import messages
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zh_77p_zd!93j)qiuoq0zhzs_u)(g$98sc@%oo_6%^penr1-04'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # 'category.apps.CategoryConfig',
    'accounts.apps.AccountsConfig',
    'blogs.apps.BlogsConfig',
    'venues.apps.VenuesConfig',
    'events.apps.EventsConfig',
    'artists.apps.ArtistsConfig',
    'pages.apps.PagesConfig',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.postgres',

    'django_cleanup.apps.CleanupConfig',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    
    'ckeditor',
    "crispy_forms",
    "crispy_bootstrap5",
    'django.contrib.humanize',
    'phonenumber_field',
]
AUTHENTICATION_BACKENDS = [
   
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
    
]
SITE_ID = 2
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
LOGIN_REDIRECT_URL='home'
ACCOUNT_EMAIL_REQUIRED = True 
ACCOUNT_AUTHENTICATION_METHOD ='username_email'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
ACCOUNT_SESSION_REMEMBER= None
# ACCOUNT_DEFAULT_HTTP_PROTOCOL ='https'
# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
      
        'APP': {
            'client_id': '556553405540-7749m72kok33589c24bibt44jnsqtbli.apps.googleusercontent.com',
            'secret': 'cW8ApkIPV8VgbJ8i9aiKO9xl',
            'key': ''
        }
    }
   
}

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Bold', 'Italic', 'Underline'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Link', 'Unlink'],
            ['RemoveFormat', 'Source']
        ],
        'width': '100%'
    },
}

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'TurnUp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS':['templates'],
        'DIRS': [BASE_DIR.joinpath('templates')],
        # 'APP_DIRS': True,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],

         'libraries':  {
                'artist_tags': 'artists.templatetags.artist_tags',
                'artist_category_tags':'artists.templatetags.artist_category_tags',
                'popular_artist_tags':'artists.templatetags.popular_artist_tags',
                # 'similar_tags':'artists.templatetags.similar_tags',
                'venues_tags':'venues.templatetags.venue_tags',
                'venue_category_tags':'venues.templatetags.venue_category_tags',
                # 'similar_tags':'venues.templatetags.similar_tags',
                'popular_venue_tags':'venues.templatetags.popular_venue_tags' ,  
                'events_tags':'events.templatetags.events_tags'   ,
                'events_category_tags':'events.templatetags.events_category_tags',
                'popular_tags':'events.templatetags.popular_tags' ,
                'category_tags':'blogs.templatetags.category_tags',
                'tag_tags':'blogs.templatetags.tag_tags',
                'recent_blogs_tags':'blogs.templatetags.recent_blogs_tags'  ,
                'search_tags':'pages.templatetags.search_tags',  
            }
        },
    },
]

WSGI_APPLICATION = 'TurnUp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'turn_up',
        'USER':'postgres',
        'PASSWORD':'23C00K1E5',
        'HOST':'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


 # Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
import os.path
STATIC_URL = '/static/'
STATIC_ROOT=  os.path.join(BASE_DIR / 'static')
STATICFILES_DIRS =[
os.path.join( BASE_DIR,'TurnUp/static'),]

#media settings
MEDIA_ROOT =  os.path.join(BASE_DIR / 'media')
MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL ='home'
LOGOUT_REDIRECT_URL ='home'
#messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
    # 50: 'critical',
}
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
