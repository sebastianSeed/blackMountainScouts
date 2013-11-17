from newsletter.models import Newsletter
from django.template import RequestContext, loader
from django.http import  *
from django.contrib.auth.decorators import login_required


@login_required
def newsletterList(request):
    template     = loader.get_template('newsletter/newsletter.html') 
    #empty context placeholder
    newsletter = Newsletter.objects.all()    
    context = RequestContext(request, {'newsletter':newsletter })
    return HttpResponse(template.render(context))