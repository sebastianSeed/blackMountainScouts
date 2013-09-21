'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from events.models import Event
from django.shortcuts import redirect

from django import forms
from easy_maps.widgets import AddressWithMapWidget

class EventAdmin(admin.ModelAdmin):
    #Remove delete selected action 
    actions = None
    #Show map widget in form
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                 'address': AddressWithMapWidget({'class': 'vTextField'})
             }



def newsletterRedirect(request):
    return redirect('/weblog/')

admin.site.register_view('newsletterRedirect','Newsletter Admin', view = newsletterRedirect)





admin.site.register(Event,EventAdmin)
