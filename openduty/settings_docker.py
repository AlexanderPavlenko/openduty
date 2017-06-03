from settings import *
import os
import dj_database_url

BASE_URL = os.environ.get('DJANGO_BASE_URL', '')
DATABASES['default'] = dj_database_url.config()
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', '')

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.ModelBackend',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
  'openduty.middleware.basicauthmiddleware.BasicAuthMiddleware',
)
