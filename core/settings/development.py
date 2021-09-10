import os.path

from .base import *

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': env('DATABASE_HOST', default=''),
            'NAME': env('DATABASE_NAME', default=''),
            'USER': env('DATABASE_USERNAME', default=''),
            'PASSWORD': env('DATABASE_PASSWORD', default=''),
            'PORT': '5432',
    }
}
