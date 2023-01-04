from .base import *

ALLOWED_HOSTS = [
    'Instagram_clone',
]




EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 25
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                       # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                       # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                       # Set to empty string for default.
    }
}

