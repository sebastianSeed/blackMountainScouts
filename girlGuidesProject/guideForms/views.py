# Create your views here.
from girlGuidesProject.guideForms.models import *
from girlGuidesProject.tables import FormsTable
from django_tables2   import RequestConfig
from django.shortcuts import render


def formList(request):
    if GuideForms.objects.all().count() > 0:
        table = FormsTable(GuideForms.objects.all())    
        RequestConfig(request).configure(table)
        return render(request, 'forms/forms.html', {'table': table})
    else:
        return render(request, 'forms/forms.html', {'noResults': True})