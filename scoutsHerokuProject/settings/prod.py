from base import *

STATICFILES_LOCATION = '/static'
STATICFILES_STORAGE = 'scoutsHerokuProject.customStorages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)