'''
Created on 07/09/2013

@author: sebastian
'''
from django.contrib import admin 
from django.contrib.comments.models import Comment
from django.contrib.sites.models import Site

##Global admin page only used for items we don't have a specific app for
#eg 3rd party includes like zinnia

#Work around to hide a model from admin without unregister it 
class commentAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

#Disable mass delete site wide as it bypasses customer model delete functions
#which contain busines rules we are enforcing
admin.site.disable_action('delete_selected')


#Register custom models
admin.site.register(Comment, commentAdmin)




