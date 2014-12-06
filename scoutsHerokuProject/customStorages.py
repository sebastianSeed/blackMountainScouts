# custom_storages.py
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

#  Custom storages classes created to split up media and  
# file storage in AMAZONS3 into 2 different folders

class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION
    
class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION