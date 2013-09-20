from django.db import models
from django.core.mail import send_mail
#Includes for email format and send
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
# Create your models here.


class Event(models.Model):
    title        = models.CharField(max_length=30)
    description  = models.CharField(max_length=100)
    start        = models.DateTimeField()
    end          = models.DateTimeField()
    

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                