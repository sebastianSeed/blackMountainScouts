'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from members.models import  scoutMember,guardian,scoutLeader
from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth.models import Group, User
from django.contrib import messages



class GuardianAdmin(admin.ModelAdmin):
    #Hide user account field as this is set by system   
    exclude = ('userAccount' ,)
 
class scoutLeaderAdmin(admin.ModelAdmin):
    #Hide user account field as this is set by system   
    exclude = ('userAccount' ,) 




class scoutAdmin(admin.ModelAdmin):
    #Set filter horizontal for searchable list of parents in admin 
    filter_horizontal = ('parents' ,)
    exclude = ('userAccount' ,) 
    




#Unregister to hide
# admin.site.unregister(Group)
# admin.site.unregister(Site)

#Register custom models
admin.site.register(scoutMember,scoutAdmin)
admin.site.register(guardian,GuardianAdmin) 
admin.site.register(scoutLeader,scoutLeaderAdmin)
#TEST



#TODO - can this be moved under project package?
### Hide all unwanted admin fields here by unregistering the groups

#Unregister fields we want to hide from admin here
#Note to get a list of all models known to ORM run 
# from django.db import models
# models.get_models()


