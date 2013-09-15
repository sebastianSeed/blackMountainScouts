'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from members.models import *
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User

# Add the employee details to the create user form in
#the framework provided admin page eg mywebsite/admin. 
class scoutMemberInline(admin.TabularInline):
    model = scoutMember
    verbose_name_plural = 'Scout troop members'




#simplify user form by removing fields

class UserAdmin(admin.ModelAdmin):
        #Override the field set options     
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),

    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1','password2')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

class GuardianAdmin(admin.ModelAdmin):
    #Hide user account field as this is set by system   
    exclude = ('userAccount' ,)
    
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)






admin.site.register(scoutMember)
admin.site.register(guardian,GuardianAdmin) 
#TEST



#TODO - can this be moved under project package?
### Hide all unwanted admin fields here by unregistering the groups









#Unregister fields we want to hide from admin here
#Note to get a list of all models known to ORM run 
# from django.db import models
# models.get_models()
admin.site.unregister(Group)
admin.site.unregister(Site)

