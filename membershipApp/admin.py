'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from membershipApp.models import *
from tagging.models import Tag,TaggedItem

# Add the employee details to the create user form in
#the framework provided admin page eg mywebsite/admin. 
class scoutMemberInline(admin.StackedInline):
    model = scoutMember
    verbose_name_plural = 'Scout troop members'

admin.site.register(scoutMember)


#TODO - can this be moved under project package?
### Hide all unwanted admin fields here by unregistering the groups
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User


#Unregister fields we want to hide from admin here
#Note to get a list of all models known to ORM run 
# from django.db import models
# models.get_models()
admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Site)

