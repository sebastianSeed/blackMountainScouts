'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from members.models import  scoutMember,guardian,scoutLeader,scoutGroups
from django.contrib import messages
from django.utils.safestring import mark_safe

class GuardianAdmin(admin.ModelAdmin):
    #Hide user account field as this is set by system   
    exclude = ('userAccount' ,)
    list_display = ('firstname','lastname',)
    readonly_fields = ('enrolled_scouts',)
    
    def enrolled_scouts(self,instance):
        linkedScoutMembers = instance.scoutmember_guardians.all()  
        displayString      = ''

        for scout in linkedScoutMembers:
            fullname           = scout.firstname + ' ' + scout.lastname
            displayString +=  "<a href= " + scout.getAdminUrl() + ">" + fullname + "</a> ,"
        mark_safe (displayString)    
        return displayString
    enrolled_scouts.allow_tags = True
    
    def delete_view(self, request, object_id,extra_context=None):
        extra_context       = extra_context or {}
        guardianObj         = self.get_object (request, object_id)
        lastParentForScout  = guardianObj.deleteWillOrphanChild()  
        extra_context['lastParentForScout'] = lastParentForScout
        if lastParentForScout:
            extra_context['scoutMembers'] = guardianObj.scoutmember_guardians.all()       
   
        return super(GuardianAdmin, self).delete_view(request, object_id,
             extra_context)
    
 
class scoutLeaderAdmin(admin.ModelAdmin):
    #Hide user account field as this is set by system   
    exclude = ('userAccount' ,) 
    list_display = ('firstname','lastname',)

#Override permissios so they can NOT delete scout groups - this is to prevent two problems
# 1) They delete a group and this delets all scouts belonging to group
# 2) Removing the 'All" scouts group which system uses to send notifications for events
#to all memebers 
class scoutGroupAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ('name','description',)


class scoutMemberAdmin(admin.ModelAdmin):
    #Set filter horizontal for searchable list of parents in admin 
    filter_horizontal = ('parents' ,)
    exclude = ('userAccount' ,) 
    list_display = ('firstname','lastname',)

    




#Unregister to hide
# admin.site.unregister(Group)
# admin.site.unregister(Site)

#Register custom models
admin.site.register(scoutMember,scoutMemberAdmin)
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


