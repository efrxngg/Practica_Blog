from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['viewsbasefunction.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'empresax',
        'USER': 'root',
        'PASSWORD': 'root1234',
        'HOST': '127.0.0.1',
        'PORT': '3307'
    }
}


