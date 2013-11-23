from django.db import models
from django.template import Context
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from members.models import scoutMember, scoutLeader , guardian

 

 
class Newsletter(models.Model):
    title                      = models.CharField(max_length=150) 
    date                       = models.DateField(auto_now=False)
    newsletter                 = models.FileField(upload_to = "newsletter" )
    #Templates for emails - can either write a whole bunch or use if statements to change wording both work -- if statements are cleaner
    newsletterEmailTemplate    =  get_template('newsletter/newsletterEmail.html')
    newsletterTxtTemplate      =  get_template( 'newsletter/newsletterEmail.txt')

    
    
    #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.title)
 
    class Meta:
        verbose_name ="Newsletter"
             
         
    def clean(self):
        if not str(self.newsletter).endswith('.pdf'):
            raise ValidationError(u'File must be a pdf')
        super(Newsletter, self).clean()  
             
              
   #Note this is called for record updates and new records inserts 
    def save(self, *args, **kwargs):  
        from_email              = 'donotreply@BlackMountainScouts.com'      
        subject                 = "New newsletter published"      
        email_destination       =  self.getEmailDestination()
        emailContext            =  Context({'body':'UPDATING AN EVENT CONTEXT'})
        #Render templates
        text_content = self.newsletterTxtTemplate.render(emailContext)
        html_content = self.newsletterEmailTemplate.render(emailContext)
        #Create and send msg
        for destination in email_destination:
            msg = EmailMultiAlternatives(subject, html_content , from_email, [destination,])
            msg.attach_alternative(text_content,"text/html")
            msg.attach_file(self.newsletter.url)
            print "URL IS  "+self.newsletter.url
            msg.send()
        super(Newsletter, self).save(*args, **kwargs)
       

         
    
    # destination must be a tuple or list eg [myDestination@test.com , ]   or   [myDestination2@test.com , ]  
    # Context must be Context object 
    def createEmailMsg(self,subject,txtTemplate,htmlTemplate,destination,context):
        htmlTemplate           =  get_template(htmlTemplate)
        plaintextTemplate      =  get_template(txtTemplate) 
        
        #Render templates
        text_content = plaintextTemplate.render(context)
        html_content = htmlTemplate.render(context)
        #Create message with html and txt formats 
        msg = EmailMultiAlternatives(subject, text_content, 'donotreply@BlackMountainScouts.com', destination)
        msg.attach_alternative(html_content,"text/html")
        return msg
        
    #Retrieve parent and scout member emails if they one and the event is for them
    #Add all scout leaders to email list            
    def getEmailDestination(self):
        scoutMembersList      = scoutMember.objects.all()
        scoutLeaders          = scoutLeader.objects.all()
        email_destination     = []
        parents               = guardian.objects.all()
        #Find appropiate scout members to email them and their guardians about event
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

                
                
                
