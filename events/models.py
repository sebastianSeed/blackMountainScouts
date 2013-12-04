from django.db import models
#Includes for email format and send
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from members.models import guardian , scoutMember, scoutGroups, scoutLeader
from django.contrib.auth.models import User
from django.utils import formats


class Event(models.Model):
    title        = models.CharField(max_length=30)
    description  = models.CharField(max_length=100)
    start        = models.DateTimeField()
    end          = models.DateTimeField()
    address      = models.CharField(max_length=100,verbose_name='Event Address') #TODO OVERWRITE SAVE LIKE IN MEMBERS APP MODELS TO SEND EMAIL 
    #Specify group so that events just for youngest group for example only get email notifications to parents/members in that group
    scoutGroup   = models.ForeignKey(scoutGroups , verbose_name="Guide group") 
    
    
    #Function to return human readable name
    def __unicode__(self):
        start =  formats.date_format(self.start, "SHORT_DATETIME_FORMAT")
        end =  formats.date_format(self.end, "SHORT_DATETIME_FORMAT")
        #return u'%s -  %s until  %s' % (self.title,start,end)
        return u'%s' % (self.title)

   
   #Note this is called for record updates and new records inserts 
    def save(self, *args, **kwargs):
        # Set up variables for email that are common to all emails 

        subject               = 'Event Updated or Created'
        from_email            = 'donotreply@BlackMountainScouts.com'      
        htmlTemplate          =  get_template('events/EventEmail.html')
        plaintextTemplate     =  get_template('events/EventEmail.txt')     
        email_destination     =  self.getEmailDestination()       
       
        
        #If the obect primary keys is not null then we are updating an existing record
        if self.pk:                        
            #Loop through sending email
            #Note - send mass email is far more efficient but does seem to support html with txt
            # fall back + implementing it was problematic 
            # Note all emails need context set here
            
            for destination in email_destination:
                emailContext = Context({'event':self, 'edit':True})
                #Render templates
                text_content = plaintextTemplate.render(emailContext)
                html_content = htmlTemplate.render(emailContext)
                #Create and send msg
                msg = EmailMultiAlternatives(subject, html_content , from_email, [destination,])
                msg.attach_alternative(html_content,"text/html")
                msg.send()

        #if not self.pk the we are creating a new event    
        else:
            emailContext = Context({'event':self, 'create':True})
            #Render templates
            text_content = plaintextTemplate.render(emailContext)
            html_content = htmlTemplate.render(emailContext)
            #Build up list of emails to send
            #Loop through sending email
            #Note - send mass email is far more efficient but does seem to support html with txt
            # fall back + implementing it was problematic 
            # Note all emails need context set here
            for destination in email_destination:
                msg = EmailMultiAlternatives(subject, html_content , from_email, [destination,])
                msg.attach_alternative(html_content,"text/html")
                msg.send()

            
        #Call parent function to fo actual saving/update
        super(Event, self).save(*args, **kwargs) 

    def delete(self, *args, **kwargs):
        email_destination     =  self.getEmailDestination()      
        if self.pk: 
            subject               = 'Event Cancelled'
            from_email            = 'donotreply@BlackMountainScouts.com'      
            htmlTemplate          =  get_template('events/EventEmail.html')
            plaintextTemplate     =  get_template('events/EventEmail.txt')     
            email_destination     =  self.getEmailDestination()                           

            #Loop through sending email
            #Note - send mass email is far more efficient but does seem to support html with txt
            # fall back + implementing it was problematic 
            # Note all emails need context set here
            for destination in email_destination:
                emailContext = Context({'event':self, 'delete':True})
                #Render templates
                text_content = plaintextTemplate.render(emailContext)
                html_content = htmlTemplate.render(emailContext)
                #Create and send msg
                msg = EmailMultiAlternatives(subject, html_content , from_email, [destination,])
                msg.attach_alternative(html_content,"text/html")
                msg.send()
        #Call parent function to fo actual saving/update
        super(Event, self).delete(*args, **kwargs) 
                        
   
    #Retrieve parent and scout member emails if they one and the event is for them
    #Add all scout leaders to email list            
    def getEmailDestination(self):
        scoutMembersList      = scoutMember.objects.all()
        scoutLeaders          = scoutLeader.objects.all()
        email_destination     = []
        parents               = []
        #Find appropiate scout members to email them and their guardians about event
        for selectedScoutMember in scoutMembersList:             
            eventScoutGroup = self.scoutGroup
            if   eventScoutGroup.name == selectedScoutMember.scoutGroup.name or eventScoutGroup.name == 'All':
                # scout member emails and accounts disabled until client confirmation
#                 if selectedScoutMember.email:
#                     email_destination.append(selectedScoutMember.email) 
#                     print email_destination
       #Get all parents for selected scout member and append to email list
                parents  = selectedScoutMember.parents.all()
                for parent in parents:            
                    if parent.email:
                        email_destination.append(parent.email)
        #Add all scout leaders to event emails
        for leader in scoutLeaders:
            if leader.email:
                email_destination.append(leader.email)
                
        #Ensure no duplicate emails - sets are guaranteed to have no duplicates
        #so type cast to set to remove duplicates - and then back to list 
        email_destination = list(set(email_destination))     
        return email_destination           

                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                