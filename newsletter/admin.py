'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from newsletter.models import *





#Register custom models
admin.site.register(gallery)
admin.site.register(newsletter)
