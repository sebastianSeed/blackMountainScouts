from base import *

#Production settings for email and file storages
# Depends on being run in heroku with environment variables set correctly
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')
DEFAULT_FROM_EMAIL = 'donotreply@BlackMountainScouts.com'

#New AMAZON S3 Settings -- Harcoded for 1st test
AWS_STORAGE_BUCKET_NAME = 'blackmountainstorage'
AWS_ACCESS_KEY_ID =  os.environ.get('AWS_SECRET_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)

# Custom class to implement static content and media content folders on amazon s3
STATICFILES_STORAGE = 'girlGuidesProject.customStorages.StaticStorage'
DEFAULT_FILE_STORAGE = 'girlGuidesProject.customStorages.MediaStorage'