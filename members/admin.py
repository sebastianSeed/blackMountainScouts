'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from members.models import  scoutMember,guardian,scoutLeader,scoutGroups
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

#Override permissios so they can NOT delete scout groups - this is to prevent two problems
# 1) They delete a group and this delets all scouts belonging to group
# 2) Removing the 'All" scouts group which system uses to send notifications for events
#to all memebers 
class scoutGroupAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False

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
admin.site.register(scoutGroups,scoutGroupAdmin) 

#TEST



#TODO - can this be moved under project package?
### Hide all unwanted admin fields here by unregistering the groups

#Unregister fields we want to hide from admin here
#Note to get a list of all models known to ORM run 
# from django.db import models
# models.get_models()


