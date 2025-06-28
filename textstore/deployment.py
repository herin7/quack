import os
import re
import sys
from .settings import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'unsafe-secret')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'


ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME', 'quacker.azurewebsites.net')]
CSRF_TRUSTED_ORIGINS = [
    f"https://{os.environ.get('WEBSITE_HOSTNAME')}",
    "https://quacker-bxaaefasc6hwh4ek.southeastasia-01.azurewebsites.net"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # serve static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Whitenoise static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Azure PostgreSQL connection
conn_str = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')

if not conn_str:
    print("⚠️ AZURE_POSTGRESQL_CONNECTIONSTRING not set — using SQLite fallback")
else:
    conn_str_params = dict(re.findall(r'([^;=]+)=([^;]+)', conn_str.strip()))
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': conn_str_params['Database'],
            'USER': conn_str_params['User Id'],
            'PASSWORD': conn_str_params['Password'],
            'HOST': conn_str_params['Server'],
            'PORT': '5432',
            'OPTIONS': {'sslmode': 'require'},
        }
    }

# Production Security Settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}

# Auth redirects
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = '/'
