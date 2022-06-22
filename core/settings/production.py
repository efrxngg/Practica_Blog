from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['viewsbasefunction.herokuapp.com']


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd9u28t2oqe8t0s',
        'USER': 'ewzhmjbvzslftm',
        'PASSWORD': '64ffae41433438fcef11eadd9964848f3e9184f3bc51cdf7197ebf03f3f87e29',
        'HOST': 'ec2-44-206-89-185.compute-1.amazonaws.com',
        'PORT': 5432,
        


    }
}


