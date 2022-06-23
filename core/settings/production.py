from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['viewsbasefunction.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db',
        'USER': 'postgre',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': 5432,
        
    }
}


PATH_GENERAL = Path(__file__).resolve().parent.parent.parent
STATICFILES_DIRS=[PATH_GENERAL.joinpath('static')]
