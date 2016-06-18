from django.template import RequestContext, loader
from django.http import  *
from django.contrib.auth.decorators import login_required
from girlGuidesProject.newsletter.models import Newsletter
from girlGuidesProject.tables import NewsletterTable
from django_tables2   import RequestConfig
from django.shortcuts import render

@login_required
def newsletterList(request):
    if Newsletter.objects.all().count() > 0:
        table = NewsletterTable(Newsletter.objects.all())    
        RequestConfig(request).configure(table)
        return render(request, 'newsletter/newsletter.html', {'table': table})
    else:
        return render(request, 'newsletter/newsletter.html', {'noResults': True})

