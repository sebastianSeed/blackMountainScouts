from django.db import models
from django.template import Context
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from members.models import scoutMember, scoutLeader , guardian, scoutGroups

 

 
class Newsletter(models.Model):
    title = models.CharField(max_length=150) 
    date = models.DateField(auto_now=False)
    newsletter = models.FileField(upload_to="newsletter")
    newsletterEmailTemplate = get_template('newsletter/newsletterEmail.html')
    newsletterTxtTemplate = get_template('newsletter/newsletterEmail.txt')
    scoutGroup = models.ForeignKey(scoutGroups , verbose_name="Guide group") 
 
        
    # Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.title)
 
    class Meta:
        verbose_name = "Newsletter"
             
         
    def clean(self):
        if not str(self.newsletter).endswith('.pdf'):
            raise ValidationError(u'File must be a pdf')
        super(Newsletter, self).clean()  
             
              
    def save(self, *args, **kwargs):  
        from_email = 'donotreply@BlackMountainScouts.com'      
        subject = "New newsletter published"      
        email_destination = self.getEmailDestination()
        emailContext = Context({'newsletterUrl':self.newsletter.url})
        text_content = self.newsletterTxtTemplate.render(emailContext)
        html_content = self.newsletterEmailTemplate.render(emailContext)
        # Create and send msg
        for destination in email_destination:
            msg = EmailMultiAlternatives(subject, html_content , from_email, [destination, ])
            msg.attach_alternative(text_content, "text/html")
            msg.send()
        super(Newsletter, self).save(*args, **kwargs)
               
    # Send newsletter to all parents and scout leaders     
    def getEmailDestination(self):
        scoutMembersList = scoutMember.objects.all()
        scoutLeaders = scoutLeader.objects.all()
        email_destination = []
        # Find appropiate scout members to email them and their guardians about event
        for selectedScoutMember in scoutMembersList:             
            newsletterScoutGroup = self.scoutGroup
            if   newsletterScoutGroup.name == selectedScoutMember.scoutGroup.name or newsletterScoutGroup.name == 'All':
                parents = selectedScoutMember.parents.all()
                for parent in parents:            
                    if parent.email:
                        email_destination.append(parent.email)
        # Add all scout leaders to event emails
        for leader in scoutLeaders:
            if leader.email:
                email_destination.append(leader.email)
                
        # Ensure no duplicate emails - sets are guaranteed to have no duplicates
        # so type cast to set to remove duplicates - and then back to list 
        email_destination = list(set(email_destination))     
        return email_destination           
                
        # Ensure no duplicate emails - sets are guaranteed to have no duplicates
        # so type cast to set to remove duplicates - and then back to list 
        email_destination = list(set(email_destination))     
        return email_destination           

                
                
                
