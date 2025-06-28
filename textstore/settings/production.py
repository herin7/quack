# textstore/settings/production.py
import os
import re
from .base import *

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'unsafe-secret')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'

ALLOWED_HOSTS = [os.environ.get('WEBSITE_HOSTNAME', 'quacker.azurewebsites.net')]
CSRF_TRUSTED_ORIGINS = [
    f"https://{os.environ.get('WEBSITE_HOSTNAME')}",
    "https://quacker-bxaaefasc6hwh4ek.southeastasia-01.azurewebsites.net",
]

# Whitenoise for static files
MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Azure PostgreSQL connection
conn_str = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')
if not conn_str:
    print("⚠️ AZURE_POSTGRESQL_CONNECTIONSTRING not set — using SQLite fallback")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
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

# Production security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'