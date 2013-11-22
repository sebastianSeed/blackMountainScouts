'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from gallery.models import Gallery 
from django.shortcuts import redirect





admin.site.register(Gallery)
