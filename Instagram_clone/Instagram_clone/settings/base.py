"""
Django settings for Instagram_clone project.
"""
from os import environ
from os.path import abspath, basename, dirname, join, normpath
from pathlib import Path
from sys import path

# PATH CONFIGURATION
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent.parent
# Absolute filesystem path to the config directory:

CONFIG_ROOT = Path(__file__).resolve(strict=True).parent.parent

# Absolute filesystem path to the project directory:
PROJECT_ROOT = Path(CONFIG_ROOT).resolve(strict=True).parent

# Absolute filesystem path to the django repo directory:
DJANGO_ROOT = Path(PROJECT_ROOT).resolve(strict=True).parent

# Project name:
PROJECT_NAME = PROJECT_ROOT.name.capitalize()

# Project folder:
PROJECT_FOLDER = PROJECT_ROOT.name

# Project domain:
PROJECT_DOMAIN = '%s.com' % PROJECT_NAME.lower()

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(str(PROJECT_ROOT))
# END PATH CONFIGURATION

DEBUG = STAGING = False
# END DEBUG CONFIGURATION

ADMINS = (
    ("""Jatin Yadav""", 'jatin.yadav@consolebit.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',  # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',  # Set to empty string for default.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_ROOT.joinpath("media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_ROOT.joinpath("assets")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT.joinpath("static"),
)


# Make this unique, and don't share it with anybody.
SECRET_KEY = environ.get('DJANGO_SECRET_KEY')

# List of callables that know how to import templates from various sources.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (PROJECT_ROOT.joinpath("templates"),),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.template.context_processors.csrf',
                'django.template.context_processors.tz',
                'django.template.context_processors.static',
                'core.context_processor.settings',
            ]
        },
    },
]

MIDDLEWARE = (
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'Instagram_clone.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'Instagram_clone.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    
    'constance',
    'constance.backends.database',
    'core',

)
CUSTOM_APPS = ['user', 'apps.base', 'apps.user_profile']

INSTALLED_APPS = list(INSTALLED_APPS) + CUSTOM_APPS

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

LOCALE_PATHS = (PROJECT_ROOT.joinpath("locale"),)

# Dummy gettext function
gettext = lambda s: s

LANGUAGES = [

('en', gettext('en')),

]


# Custom User Model
AUTH_USER_MODEL = 'user.User'
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django Constance
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'
CONSTANCE_CONFIG = {
    'SITE_NAME': ('Website title', ''),
    'SITE_DESCRIPTION': ('Website description', ''),
    'ADDRESS': ('Address', ''),
    'PHONE': ('Phone', ''),
    'EMAIL': ('Email', ''),
    'FACEBOOK': ('Facebook URL', ''),
    'INSTAGRAM': ('Instagram URL', ''),
    'TWITTER': ('Twitter URL', ''),
    'LINKEDIN': ('Linkedin URL', ''),
    'GOOGLE_ANALYTICS': ('UA-XXXXXXXXX-X', ''),
    'GOOGLE_TAG_MANAGER': ('GTM-XXXXXXX', ''),
    'GOOGLE_SITE_VERIFICATION': ('XXXXXXXXXXX', ''),
}

CONSTANCE_CONFIG_FIELDSETS = {
    'Website Detail': ('SITE_NAME', 'SITE_DESCRIPTION', 'ADDRESS', 'PHONE', 'EMAIL'),
    'Social Options': ('FACEBOOK', 'INSTAGRAM', 'TWITTER', 'LINKEDIN'),
    'SEO': ('GOOGLE_ANALYTICS', 'GOOGLE_TAG_MANAGER', 'GOOGLE_SITE_VERIFICATION')
}

LOGOUT_REDIRECT_URL = 'login'

LOGIN_REDIRECT_URL = 'home'


