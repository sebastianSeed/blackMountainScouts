import django_tables2 as tables
from events.models import Event          
from newsletter.models import Newsletter
from django.utils.safestring import SafeString
class EventsTable(tables.Table):
#     id  = tables.URLColumn()
    class Meta:
        model     = Event
        #sequence  = ("title", "description","start","end","address","scoutGroup","id")
#     
#     def render_id(self, value):
#         link   = SafeString("<a href='/events/id=%s'>Details</a>" % value)
#         link   = SafeString(link)
        
        
class NewsletterTable(tables.Table):
    class Meta:
        model = Newsletter
        
        
        
        