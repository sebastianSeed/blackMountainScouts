'''
Created on 09/09/2013

@author: sebastian
'''

from django.http import  *
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth import logout,authenticate, login, logout
from django.shortcuts import render_to_response,redirect
from events.models import Event


def home(request):
    template     = loader.get_template('scoutsHerokuProject/home.html') 
    #empty context placeholder
    events = Event.objects.all()    
    context = RequestContext(request, {'events':events})
    return HttpResponse(template.render(context))

#when user logs out redirect them to home page
def logoutView(request):
    logout(request)
    return redirect('scoutsHerokuProject.views.home')


