from events.models import Event
from django.template import RequestContext, loader
from django.http import  *
from django.contrib.auth.decorators import login_required

@login_required
def eventList(request):
    template     = loader.get_template('events/events.html') 
    events = Event.objects.all()    
    context = RequestContext(request, {'events':events, })
    return HttpResponse(template.render(context))

@login_required
def eventDetail(request , id = 1):
    template     = loader.get_template('events/eventDetail.html') 
    try:
        event   = Event.objects.get(id = id)    
        context = RequestContext(request, {'event':event, })
    except():
        context = RequestContext(request,{'noResults':True})
        
    return HttpResponse(template.render(context))