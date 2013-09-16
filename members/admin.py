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
    #Create a read only field to display enrolled children
    #Do no allow children adding here to prevent loop (to add a child they must have parent)
#    readonly_fields = ('Enrolled_Children',)
    
#     def getRelatedChildren(self):
#         resultQuerySet =  scoutMember.objects.prefetch_related('parent').filter(parents = self)
#         resultsString  = ''
#         if resultQuerySet.exists():
#             for e in resultQuerySet:
#                 resultsString += e.firstname + ' ' + e.lastname +', '
#             return resultsString
#         else:
#             return "TODO DEBUG ME"
#         
#     def Enrolled_Children(self, instance):
#         querySet = scoutMember.objects.filter(parents = self.pk)
#         childList = ""
#         for obj in querySet:
#             childList += obj.firstname + ' ' + obj.lastname
#         return childList
#     
#     Enrolled_Children.short_description ="Enrolled Chidren"


    
    



class scoutAdmin(admin.ModelAdmin):
    #Set filter horizontal for searchable list of parents in admin 
    filter_horizontal = ('parents' ,)

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
admin.site.register(scoutMember,scoutAdmin)
admin.site.register(guardian,GuardianAdmin) 
#TEST



#TODO - can this be moved under project package?
### Hide all unwanted admin fields here by unregistering the groups









#Unregister fields we want to hide from admin here
#Note to get a list of all models known to ORM run 
# from django.db import models
# models.get_models()


