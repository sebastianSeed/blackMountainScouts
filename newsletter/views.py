from newsletter.models import Newsletter
from django.template import RequestContext, loader
from django.http import  *
from django.contrib.auth.decorators import login_required


@login_required
def newsletterList(request):
    template     = loader.get_template('newsletter/newsletter.html') 
    #empty context placeholder
    newsletters  = Newsletter.objects.all()    
    context      = RequestContext(request, {'newsletters':newsletters })
    return HttpResponse(template.render(context))

@login_required
def newsletterDetail(request , id = 1):
    template     = loader.get_template('events/newsletterDetail.html') 
    try:
        event   = Newsletter.objects.get(id = id)    
        context = RequestContext(request, {'event':event, })
    except():
        context = RequestContext(request,{'noResults':True})
        
    return HttpResponse(template.render(context))