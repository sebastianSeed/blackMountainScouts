'''
Created on 21/09/2013

@author: sebastian
'''
from django.db import models
from zinnia.models.entry import EntryAbstractClass
from django.template.loader import get_template
from members.models import guardian , scoutMember, scoutGroups, scoutLeader
from django.template import Context
from django.core.mail import EmailMultiAlternatives


class EntryNotification(EntryAbstractClass):
    

   #Note this is called for record updates and new records inserts 
    def save(self, *args, **kwargs):
        # Set up variables for email that are common to all emails 

        subject               = 'Event Updated or Created'
        from_email            = 'donotreply@BlackMountainScouts.com'      
        htmlTemplate          =  get_template('events/EventEmail.html')
        plaintextTemplate     =  get_template('events/EventEmail.txt')     
        email_destination     =  self.getEmailDestination()       
       
        
        #If the obect primary keys is  null then this is a new post
        if self.pk is  None:    
             
            for destination in email_destination:
                emailContext = Context({'body':'UPDATING AN EVENT CONTEXT'})
                #Render templates
                text_content = plaintextTemplate.render(emailContext)
                html_content = htmlTemplate.render(emailContext)
                #Create and send msg
                msg = EmailMultiAlternatives(subject, html_content , from_email, [destination,])
                msg.attach_alternative(html_content,"text/html")
                msg.send()
                print "SENT MESSAGE !!!!!!!!!!!!!!!!!!!!!!!!!!!!1"

           
        #Call parent function to fo actual saving/update
        super(EntryNotification, self).save(*args, **kwargs) 

                       
   
    #Retrieve parent and scout member emails if they one and the event is for them
    #Add all scout leaders to email list            
    def getEmailDestination(self):
        scoutMembersList      = scoutMember.objects.all()
        scoutLeaders          = scoutLeader.objects.all()
        parents               = guardian.objects.all()
        email_destination     = []
        #Send email too members , parents and scout leaders
        for selectedScoutMember in scoutMembersList:             
                if selectedScoutMember.email:
                    email_destination.append(selectedScoutMember.email) 
        for parent in parents:            
            if parent.email:
                email_destination.append(parent.email)

        for leader in scoutLeaders:
            if leader.email:
                email_destination.appent(leader.email)
                
        #Ensure no duplicate emails - sets are guaranteed to have no duplicates
        #so type cast to set to remove duplicates - and then back to list 
        email_destination = list(set(email_destination))     
        return email_destination
 
                
    class Meta(EntryAbstractClass.Meta):
        abstract = True
