from django.db import models
from django.core.mail import send_mail
#Includes for email format and send
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
# Import member and user models to get email for notifications
from members.models import guardian,scoutMember
from django.contrib.auth.models import User


class Event(models.Model):
    title        = models.CharField(max_length=30)
    description  = models.CharField(max_length=100)
    start        = models.DateTimeField()
    end          = models.DateTimeField()
    
#TODO OVERWRITE SAVE LIKE IN MEMBERS APP MODELS TO SEND EMAIL 
#USE A FEW TEMPLATES FOR ADD/EDIT /DELETE
   #Note this is called for record updates and new records inserts 
    def save(self, *args, **kwargs):
        # Set up variables for email that are common to all emails 

        subject    = 'Account Created or Updated'
        from_email = 'donotreply@BlackMountainScouts.com'
        
        
        scoutMembers   = scoutMember.objects.all()
        parents        = guardian.objects.all()
        
        
        
        #If the obect primary keys is not null then we are updating an existing record

        if self.pk is not None:                        
            emailContext = Context({'body':'EDIT EMAIL TEMPLATE'})
            htmlTemplate          =  get_template('events/EditEventEmail.html')
            plaintextTemplate      =  get_template('events/EditEventEmail.txt') 
            #Render templates
            text_content = plaintextTemplate.render(emailContext)
            html_content = htmlTemplate.render(emailContext)
            
            
            originalObject = guardian.objects.get(pk = self.pk)
            #Change account details if we have changed firstname and lastname
            if self.firstname != originalObject.firstname or self.lastname != originalObject.lastname:
                user             = originalObject.userAccount
                user.username    = username.lower()
#                 user.is_staff = True
                user.save()
                user.set_password (password)
                user.save()
                #Send confirmation email if customer has email
                if self.email:
#                     send_mail(subject , body, from_email, [self.email])  
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [self.email])
                    msg.attach_alternative(html_content,"text/html")
                    msg.send()
            # Call original save() method to do DB updates/inserts
            super(guardian, self).save(*args, **kwargs) 
        #If not self.pk - we are creating new entry
        else:
            user = User.objects.create_user(username, '', password) 
            user.save()
            self.userAccount  = user 
            super(guardian, self).save(*args, **kwargs) 
            if self.email:
                #                     send_mail(subject , body, from_email, [self.email])  
                    msg = EmailMultiAlternatives(subject, text_content, from_email, [self.email])
                    msg.attach_alternative(html_content,"text/html")
                    msg.send()
                        
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                