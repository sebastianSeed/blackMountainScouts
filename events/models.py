from django.db import models
from django.core.mail import send_mail


# Create your models here.


class Event(models.Model):
    title        = models.CharField(max_length=30)
    description  = models.CharField(max_length=100)
    start        = models.DateTimeField()
    end          = models.DateTimeField()
    
    def save(self):
        super(Event, self).save()
        #TODO GET THIS FORMATTED NICELY AND SPLIT INTO A FUCNTION 
        # Reuse it over in FORUM customisation eg zinniaBlogCustomisation.py
        send_mail('TEST SUBJECT', 'Here is the message.', 'from@example.com',
                ['to@example.com'], fail_silently=False)