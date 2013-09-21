'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from events.models import Event

from django import forms
from easy_maps.widgets import AddressWithMapWidget

class EventAdmin(admin.ModelAdmin):
    class form(forms.ModelForm):
        class Meta:
            widgets = {
                'address': AddressWithMapWidget({'class': 'vTextField'})
            }









admin.site.register(Event,EventAdmin)
