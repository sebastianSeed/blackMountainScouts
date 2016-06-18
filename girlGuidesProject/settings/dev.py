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



DEBUG =  True


STATIC_URL = '/static/'
#add debug toolbar for dev




