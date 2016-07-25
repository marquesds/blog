from .base import *


SECRET_KEY = get_secret('local', 'SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DB_CONF = get_secret('local', 'DATABASE')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_CONF.get('DB_NAME'),
        'USER': DB_CONF.get('DB_USER'),
        'PASSWORD': DB_CONF.get('DB_PWD'),
        'HOST': DB_CONF.get('DB_HOST'),
        'PORT': DB_CONF.get('DB_PORT'),
    }
}
