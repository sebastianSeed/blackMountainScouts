'''
Created on 16/11/2013

@author: sebastian
'''

#Subclass built in contact form plugin to send to all scout leaders
from envelope.forms import ContactForm

class MyContactForm(ContactForm):
    subject_intro = "URGENT: "
    template_name = "contact_email.html"