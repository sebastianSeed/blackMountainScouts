from events.models import Event
from django.template import RequestContext, loader
from django.http import  *
from django.contrib.auth.decorators import login_required


@login_required
def eventList(request):
    template     = loader.get_template('events/events.html') 
    #empty context placeholder
    events = Event.objects.all()    
    context = RequestContext(request, {'events':events })
    return HttpResponse(template.render(context))