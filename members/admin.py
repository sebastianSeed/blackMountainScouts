'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin
from members.models import  scoutMember,guardian,scoutLeader,scoutGroups
from django.utils.safestring import mark_safe
from django.contrib.admin import ModelAdmin, SimpleListFilter
from django.contrib import messages







class GuardianAdmin(admin.ModelAdmin):
    #Hide user account field as this is set by system   
    exclude = ('userAccount' ,)
    list_display = ('firstname','lastname',)
    readonly_fields = ('enrolled_scouts',)
    #Read only field with names of enrolled scouts for a parent 
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
    
 
class scoutLeaderAdmin(ModelAdmin):
    #Hide user account field as this is set by system   
    search_fields = ('firstname',)
    exclude = ('userAccount' ,) 
    list_display = ('firstname','lastname',)
    sortable ='order'



#Override permissions so they can NOT delete scout groups - this is to prevent two problems
# 1) They delete a group and this delets all scouts belonging to group
# 2) Removing the 'All" scouts group which system uses to send notifications for events
#to all memebers 
class scoutGroupAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj=None):
        return False
    list_display = ('name','description',)

    def save_model(self, request, obj, form, change):
        messages.add_message(request, messages.INFO, 'Hello world.')
        super(scoutGroupAdmin,self).save_model(request, obj, form, change)


class scoutMemberAdmin(admin.ModelAdmin):
    #Set filter horizontal for searchable list of parents in admin 
    filter_horizontal = ('parents' ,)
    exclude = ('userAccount' ,) 
    list_display = ('firstname','lastname',)

    

#Register custom models
admin.site.register(scoutMember,scoutMemberAdmin)
admin.site.register(guardian,GuardianAdmin) 
admin.site.register(scoutLeader,scoutLeaderAdmin)
admin.site.register(scoutGroups,scoutGroupAdmin) 



