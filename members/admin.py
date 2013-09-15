'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from members.models import  scoutMember,guardian
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User



class GuardianAdmin(admin.ModelAdmin):
    #Hide user account field as this is set by system   
    exclude = ('userAccount' ,)


#simplify user form by removing fields

class customUser(admin.ModelAdmin):
        #Override the field set options     
    fieldsets = (
        (None, {'fields': ('username', 'password','first_name','last_name')}),
         
 
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1','password2','first_name','last_name')}),
        
    )




#Unregister to hide
admin.site.unregister(Group)
admin.site.unregister(Site)

#Register custom models
admin.site.register(scoutMember)
admin.site.register(guardian,GuardianAdmin) 
#TEST



#TODO - can this be moved under project package?
### Hide all unwanted admin fields here by unregistering the groups









#Unregister fields we want to hide from admin here
#Note to get a list of all models known to ORM run 
# from django.db import models
# models.get_models()


