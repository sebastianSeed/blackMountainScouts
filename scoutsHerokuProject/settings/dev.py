from scoutsHerokuProject.settings.base import *

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
