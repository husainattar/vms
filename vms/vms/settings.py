"""
Django settings for vms project.

Note: Currently development settings. Not suitable as is for production.
"""
from django.urls import reverse_lazy
from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from decouple import config
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')


# SECURITY WARNING: run with debug turned off (DEBUG = False) in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# Application definition
INSTALLED_APPS = (
    'authentication',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'administrator',
    'event',
    'home',
    'job',
    'organization',
    'registration',
    'shift',
    'volunteer',
    'cities_light',
    'pom',
    'rest_framework',
    'easy_pdf',
    'vms',
)

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'vms.urls'

WSGI_APPLICATION = 'vms.wsgi.application'

# Database
# Change these database settings if your database engine, database name,
# username or password changes
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),  # Edit 'postgres' while running docker
        'USER': config('DB_USER'),  # Edit 'postgres' while running docker
        'PASSWORD': config('DB_PASSWORD'),  # Edit 'mysecretpassword' while running docker
        'HOST': config('DB_HOST'),  # Edit 'db' while running docker
        'PORT': 5432

    }
}


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


# Internationalization
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale/'), )

LANGUAGES = (
    ('en-us', _('English')),
    ('fr-fr', _('French')),
)

# Static files (CSS, JavaScript, Images)
# Specifies the directory where static files (CSS, JavasScript) are stored
STATIC_URL = '/static/'

# All uploaded files (such as resumes) are stored in the /srv directory
# /srv directory contains site-specific data which is served by the system
MEDIA_ROOT = os.path.join(BASE_DIR, 'srv')
MEDIA_URL = '/srv/'

# Uploaded files have read and write permissions to the owner only
FILE_UPLOAD_PERMISSIONS = 0o740

FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o740

# If user fails to authenticate, then they are redirected to the view
# specified in the reverse_lazy call
LOGIN_URL = reverse_lazy('authentication:login_process')

STATIC_ROOT = './static/'

# Instead of sending out real email, during development the emails will be sent
# to stdout, where from they can be inspected.
if DEBUG:
    EMAIL_HOST = config('EMAIL_HOST', default='localhost')
    EMAIL_PORT = config('EMAIL_PORT', default=1025, cast=int)
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

LOGIN_REDIRECT_URL = reverse_lazy('home:index')
RECOVER_ONLY_ACTIVE_USERS = False
ACCOUNT_ACTIVATION_DAYS = 2
ANONYMOUS_USER_ID = -1

