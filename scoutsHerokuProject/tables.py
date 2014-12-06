import django_tables2 as tables
from events.models import Event          
from newsletter.models import Newsletter
from django.utils.safestring import SafeString
from guideForms.models import GuideForms
from django_tables2.columns.templatecolumn import TemplateColumn

# Used to display tables to non admin users , upcoming events , newsletters and forms

class EventsTable(tables.Table):
    address = TemplateColumn("<a href='/events/id=" + '{{ record.id }}'  + "'>" + '{{record.address}}' + "</a>")
    class Meta:
        model = Event

        
        
class NewsletterTable(tables.Table):
    class Meta:
        model = Newsletter
        

class FormsTable(tables.Table):
    class Meta:
        model = GuideForms        
        
        