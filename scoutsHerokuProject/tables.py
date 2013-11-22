import django_tables2 as tables
from events.models import Event          
from newsletter.models import Newsletter
from django.utils.safestring import SafeString

        
class EventsTable(tables.Table):

    class Meta:
        model = Event
    def render_address(self,value):
        return SafeString("<a href='/events/address=" + value + "'>" + value + "</a>")
        
   
        
class NewsletterTable(tables.Table):
    class Meta:
        model = Newsletter
        
        
        
        