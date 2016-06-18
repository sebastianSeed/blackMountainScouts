'''
Created on 17/09/2013

@author: sebastian
'''

from girlGuidesProject.members.models import scoutLeader

# Function to only display whitelisted apps in the admin page , this 
# was created to prevent third party apps showing in user facing AdminSite
def custom_discover(whitelist):
    import copy
    from django.conf import settings
    from django.utils.importlib import import_module
    from django.utils.module_loading import module_has_submodule
    from django.contrib.admin.sites import AdminSite, site
    for app in whitelist:
        mod = import_module(app)
        # Attempt to import the app's admin module.
        try:
            before_import_registry = copy.copy(site._registry)
            import_module('%s.admin' % app)
        except:
            # Reset the model registry to the state before the last import as
            # this import will have to reoccur on the next request and this
            # could raise NotRegistered and AlreadyRegistered exceptions
            # (see #8245).
            site._registry = before_import_registry

            # Decide whether to bubble up this error. If the app just
            # doesn't have an admin module, we can ignore the error
            # attempting to import it, otherwise we want it to bubble up.
            if module_has_submodule(mod, 'admin'):
                raise
            
def getScoutLeaders():
    scoutLeaders          = scoutLeader.objects.all()
    email_destination    = []
    #Add all scout leaders to event emails
    for leader in scoutLeaders:
        if leader.email:
            email_destination.append(leader.email)
    return email_destination