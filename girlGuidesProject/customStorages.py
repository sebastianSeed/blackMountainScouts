# custom_storages.py
from django.conf import settings
from storages.backends.s3boto import S3BotoStorage

#  Custom storages classes created to split up media and  
# file storage in AMAZONS3 into 2 different folders
# Implemented path function to avoid not implemented error created when botostorage plugin
# is used with photologue on amazon S3 
class StaticStorage(S3BotoStorage):
    location = settings.STATICFILES_LOCATION
    def path(self, name):
        return settings.STATICFILES_LOCATION
    
class MediaStorage(S3BotoStorage):
    location = settings.MEDIAFILES_LOCATION
    def path(self, name):
        return settings.MEDIAFILES_LOCATION