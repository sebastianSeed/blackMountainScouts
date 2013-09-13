'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from members.models import *

# Add the employee details to the create user form in
#the framework provided admin page eg mywebsite/admin. 
class scoutMemberInline(admin.TabularInline):
    model = scoutMember
    verbose_name_plural = 'Scout troop members'

class guardianAdmin(admin.ModelAdmin):
     inlines = [
        scoutMemberInline,
    ]



admin.site.register(scoutMember)
admin.site.register(guardian) 
#TEST


#TODO - can this be moved under project package?
### Hide all unwanted admin fields here by unregistering the groups
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User


#Unregister fields we want to hide from admin here
#Note to get a list of all models known to ORM run 
# from django.db import models
# models.get_models()
admin.site.unregister(Group)
admin.site.unregister(Site)

