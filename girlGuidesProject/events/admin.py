'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from girlGuidesProject.events.models import Event
from django.shortcuts import redirect
from girlGuidesProject.settings import dev

#Includes for map widget in events address
from django import forms
from easy_maps.widgets import AddressWithMapWidget


class EventAdmin(admin.ModelAdmin):
    #Remove delete selected action 
    actions = None
    
    class Media:
        js = [
            'http://code.jquery.com/jquery-1.4.2.min.js',
            'http://maps.google.com/maps/api/js?sensor=false',
            dev.STATIC_URL +'/main/js/google-maps-plugin.js'
        ]

admin.site.register(Event,EventAdmin)