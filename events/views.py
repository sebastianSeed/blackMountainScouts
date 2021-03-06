from events.models import Event
from django.template import RequestContext, loader
from django.http import  *
from django.contrib.auth.decorators import login_required
from scoutsHerokuProject.tables import EventsTable
from django_tables2   import RequestConfig
from django.shortcuts import render
from datetime import datetime

@login_required
def eventList(request):
    if Event.objects.all().count() > 0:
        curEvents = Event.objects.filter(end__gte=datetime.today())
        table = EventsTable(curEvents)    
        RequestConfig(request).configure(table)
        return render(request, 'events/events.html', {'table': table, 'events':curEvents})
    else:
        return render(request, 'events/events.html', {'noResults': True})


@login_required
def eventDetail(request , id = 1 ):
    event        = Event.objects.get(pk = id)
    template     = loader.get_template('events/eventDetail.html') 
    context      = RequestContext(request,{'event':event})
        
    return HttpResponse(template.render(context))