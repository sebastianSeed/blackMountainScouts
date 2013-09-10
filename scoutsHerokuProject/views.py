'''
Created on 09/09/2013

@author: sebastian
'''

from django.http import  HttpResponse
from django.template import RequestContext, loader

def home(request):
    template     = loader.get_template('scoutsHerokuProject/home.html') 
    #empty context placeholder
    context = RequestContext(request, {})
    return HttpResponse(template.render(context))