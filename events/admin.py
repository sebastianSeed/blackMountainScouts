'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from events.models import Event
from django.shortcuts import redirect

#Includes for map widget in events address
from django import forms
from easy_maps.widgets import AddressWithMapWidget


class EventAdmin(admin.ModelAdmin):
    #Remove delete selected action 
    actions = None




admin.site.register(Event,EventAdmin)
