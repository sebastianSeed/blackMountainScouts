from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'mysecretpassword',
        'HOST': 'postgres',
        'PORT': '',
    }
}
DEBUG = 'TRUE'
STATICFILES_LOCATION = 'static'
STATIC_URL = '/static/'
