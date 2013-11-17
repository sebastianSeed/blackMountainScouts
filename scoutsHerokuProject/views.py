'''
Created on 09/09/2013

@author: sebastian
'''

from django.http import  *
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from django.shortcuts import redirect
from events.models import Event
from newsletter.models import Gallery 


# from envelope.views import ContactView
# 
# class CustomContactForm(ContactView):
#     subject_intro = "URGENT: "
#     template_name = "contact_email.html"


def home(request):
    template     = loader.get_template('main/home.html') 
    #empty context placeholder
    images = Gallery.objects.filter(public=True)
    events = Event.objects.all()    
    context = RequestContext(request, {'events':events , 'publicImages':images})
    return HttpResponse(template.render(context))

#when user logs out redirect them to home page
def logoutView(request):
    logout(request)
    return redirect('scoutsHerokuProject.views.home')


