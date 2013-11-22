import django_tables2 as tables
from events.models import Event          
from newsletter.models import Newsletter

class EventsTable(tables.Table):
    Details  = tables.TemplateColumn("<a href='/events/id={{Event.ID}}'>Details</a>")
    data = [
            {"Name": "Bradley"},
            {"Title": "Stevie"},
            {"Description": "Bradley"},
            {"Start": "Stevie"},
            {"End": "Bradley"},
            {"Location": "Stevie"},
            {"Scout Group": "Stevie"},
            {"Details": "Stevie"},
            
            
            ]
    class Meta:
        model = Event


class NewsletterTable(tables.Table):
    class Meta:
        model = Newsletter
        