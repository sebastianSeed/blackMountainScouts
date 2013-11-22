'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from newsletter.models import *


class newsLetterAdmin(admin.ModelAdmin):
   
    #pass flag so we can add extra confirmation steps when user is publishing a newsletter as this triggers email
    def add_view(self, request, form_url='', extra_context=None):
        extra_context       = extra_context or {}
        extra_context['confirmSave'] = True   
        return super(newsLetterAdmin, self).add_view(request, form_url, extra_context)


#Register custom models
admin.site.register(Newsletter,newsLetterAdmin)
