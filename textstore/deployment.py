import os
import re
from .settings import BASE_DIR

# Override secret key & debugging
SECRET_KEY = os.environ['SECRET']
DEBUG = False

# Configure allowed hosts from Azure environment
ALLOWED_HOSTS = [os.environ['WEBSITE_HOSTNAME']]
CSRF_TRUSTED_ORIGINS = ['https://' + os.environ['WEBSITE_HOSTNAME']]

# WhiteNoise middleware for serving static files
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

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Azure PostgreSQL connection string
conn_str = os.environ.get('AZURE_POSTGRESQL_CONNECTIONSTRING')

if not conn_str:
    print("⚠️ AZURE_POSTGRESQL_CONNECTIONSTRING not set — using SQLite fallback")
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
else:
    # Parse Azure connection string
    conn_str_params = dict(re.findall(r'([^;=]+)=([^;]+)', conn_str.strip()))
    
    required_keys = ['Database', 'User Id', 'Password', 'Server']
    if not all(k in conn_str_params for k in required_keys):
        raise ValueError("❌ Invalid connection string: missing required parameters")

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': conn_str_params['Database'],
            'USER': conn_str_params['User Id'],
            'PASSWORD': conn_str_params['Password'],
            'HOST': conn_str_params['Server'],
            'PORT': '5432',
            'OPTIONS': {
                'sslmode': 'require',
            },
        }
    }

# HTTPS and SSL security settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
