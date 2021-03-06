from .base import *

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]', 'hillside-app.ue.r.appspot.com']

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

if os.environ.get("GOOGLE_CLOUD_PROJECT", None):
    DATABASES["default"]["HOST"] = env('CLOUD_SQL_URL', default='')

# Allows logging to the console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG',
    },
}
