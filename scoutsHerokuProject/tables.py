import django_tables2 as tables
from events.models import Event          
from newsletter.models import Newsletter

class EventsTable(tables.Table):
    kd  = tables.URLColumn()
    class Meta:
        model = Event

    def render_details(self, value):
        return "<a href='/events/id=%s'>Details</a>" % value

class NewsletterTable(tables.Table):
    class Meta:
        model = Newsletter
        