from django.db import models
from django.core.mail import send_mail
#Includes for email format and send
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
# Import member and user models to get email for notifications
from members.models import guardian , scoutMember, scoutGroups, scoutLeader
from django.contrib.auth.models import User


class Event(models.Model):
    title        = models.CharField(max_length=30)
    description  = models.CharField(max_length=100)
    start        = models.DateTimeField()
    end          = models.DateTimeField()
    address      = models.CharField(max_length=100,verbose_name='Event Address') #TODO OVERWRITE SAVE LIKE IN MEMBERS APP MODELS TO SEND EMAIL 
    #Specify group so that events just for youngest group for example only get email notifications to parents/members in that group
    scoutGroup   = models.ForeignKey(scoutGroups , verbose_name="Scout group") 




   #Note this is called for record updates and new records inserts 
    def save(self, *args, **kwargs):
        # Set up variables for email that are common to all emails 

        subject    = 'Account Created or Updated'
        from_email = 'donotreply@BlackMountainScouts.com'
        
        scoutMembersList      = scoutMember.objects.all()
        scoutLeaders          = scoutLeader.objects.all()
        htmlTemplate          =  get_template('events/EventEmail.html')
        plaintextTemplate     =  get_template('events/EventEmail.txt')     
        
        email_destination    = []
        #Find appropiate scout members to email them and their guardians about event
        for selectedScoutMember in scoutMembersList:
             
            eventScoutGroup = self.scoutGroup
            if   eventScoutGroup.name == selectedScoutMember.scoutGroup.name or eventScoutGroup.name == 'All':
                #Note we check parent and child email seperately as  both may or may not exist
                if selectedScoutMember.email:
                    email_destination += selectedScoutMember.email        
                parent  = selectedScoutMember.guardian            
                if parent.email:
                    email_destination += parent.email
        #Add all scout leaders to event emails
        for leader in scoutLeaders:
            if leader.email:
                email_destination += leader.email
        
        #Ensure no duplicate emails - sets are guarnteed to have no duplicates
        #so type cast to set to remove duplicates - and then back to list 
            email_destination = list(set(email_destination))
        
        
        #If the obect primary keys is not null then we are updating an existing record
        if self.pk is not None:                        
            emailContext = Context({'body':'UPDATING AN EVENT CONTEXT'})
            #Render templates
            text_content = plaintextTemplate.render(emailContext)
            html_content = htmlTemplate.render(emailContext)

            #TODO LOOP OVER AND GET EMAILS FOR DESTINATIONS -- USE BCC for privacy
#TODO CONSIDER MAKING A BUNCH OF EMAILS INSTEAD OF BCC AND USING SENDMASSMAIL FUNCTIOn
            msg = EmailMultiAlternatives( subject, text_content, from_email, bcc = email_destination)
            msg.attach_alternative(html_content,"text/html")
            msg.send()
        #if not self.pk the we are creating a new event    
        else:
            emailContext = Context({'body':'UPDATING AN EVENT CONTEXT'})
            #Render templates
            text_content = plaintextTemplate.render(emailContext)
            html_content = htmlTemplate.render(emailContext)
            #TODO LOOP OVER AND GET EMAILS FOR DESTINATIONS -- USE BCC for privacy
            msg = EmailMultiAlternatives( subject, text_content, from_email, bcc = email_destination)
            msg.attach_alternative(html_content,"text/html")
            msg.send()
            
        #Call parent function to fo actual saving/update
        super(Event, self).save(*args, **kwargs) 

                        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                