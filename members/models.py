from django.db import models
from django.core.validators import RegexValidator, validate_email
from django.contrib.auth.models import User
from django.core.mail import send_mail
from  django.contrib.auth.models import AbstractUser
# Create your models here.

#TODO MODEL FOR ADMINS? Extend users + give them rights to edit everything -- eg forum newsletters etc
class scoutMember(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=100)
    dob       = models.DateField(verbose_name='birthday')
    parents   = models.ManyToManyField('guardian', related_name = 'scoutmember_guardians')
    
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)

    class meta:
        unique_together = ("firstname", "lastname")
      


class guardian(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=100)
    phone = models.IntegerField(
                                            validators=[RegexValidator(
                                                                    r'^[0-9]{8,12}',
                                                                    'Phone numbers must be 8-12 digits.',
                                                                    'Invalid Number'),
                                                       ],) 
   # kids        = models.ManyToManyField('scoutMember', through=scoutMember.parents.through)
    email       = models.CharField(max_length=100, validators = [validate_email], blank = True)
    userAccount = models.OneToOneField(User)
    #Records must have unique firstname and last name combo so we get unique usernames
    class meta:
        unique_together = ("firstname", "lastname")
        
    #TODO If parent is last guardian for a scout then raise message and delete scout if confirmed
#     ### THIS NEEDS TO GO INTO VIEW - OVERWRITE DELETE VIEW FOR ADMIN GUARDIANS
#     def delete(self, *args, **kwargs):
#         super(guardian, self).delete(*args, **kwargs)
#         #If only 1 kid left
#         if len(self.scoutmember_guardians.all()) == 1:
#             messages.add_message(request, messages.ERROR, 'Woah there - you are about to delete the last parent a current member has!.')
# 
#             
        
         
   #Note this is called for record updates and new records inserts 
    def save(self, *args, **kwargs):
        # Set notification email text
        body = """
        Hello {name},
        Your user account has been updated or created,
        Username:{username}
        Password:{password} 
        You can use these details to logon onto the scout's website  at http://blackmountainscouts.herokuapp.com
        Please do not reply to this email as this inbox is not monitored.
        Thank you 
        
        """
        #Generate username and password for email and account update/creation
        username = self.firstname +'_'+self.lastname
        password = username
        body = body.format(name = self.firstname, username = username, password = password)    
        

        #If the obect primary keys is not null then we are updating an existing record
        #Check if we need to update sit logon details
        if self.pk is not None:
            originalObject = guardian.objects.get(pk = self.pk)
            #Change account details if we have changed firstname and lastname
            if self.firstname != originalObject.firstname or self.lastname != originalObject.lastname:
                user             = originalObject.userAccount
                user.username    = username
#                 user.is_staff = True
                user.save()
                user.set_password (password)
                user.save()
                # Call original save() method to do DB updates/inserts
                super(guardian, self).save(*args, **kwargs) 
                #Send confirmation email if customer has email
                if self.email:
                    send_mail('Account Updated', body, 'admin@BlackMountainScouts.com', [self.email])   
        #If not self.pk - we are creating new entry
        else:
            user = User.objects.create_user(username, '', password) 
            user.save()
            self.userAccount  = user 
            super(guardian, self).save(*args, **kwargs) 
            if self.email:
                send_mail('Account Created', body, 'admin@BlackMountainScouts.com', [self.email])
        
      
            

            
                        
                
    
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)
    

                      




