import django_tables2 as tables
from events.models import Event          
from newsletter.models import Newsletter

class EventsTable(tables.Table):
    Details  = tables.TemplateColumn("<a href='/events/id={{Event.ID}}'>Details</a>")
    class Meta:
        model = Event


class NewsletterTable(tables.Table):
    Download  = tables.TemplateColumn("<a href='/events/id={{Newsletter.ID}}'>Download</a>")
    class Meta:
        model = Newsletter
        