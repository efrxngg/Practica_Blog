from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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


PATH_GENERAL = Path(__file__).resolve().parent.parent.parent
STATICFILES_DIRS=[PATH_GENERAL.joinpath('static')]