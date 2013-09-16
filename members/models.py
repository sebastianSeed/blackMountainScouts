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
    parents   = models.ManyToManyField('guardian', related_name = 'guardiansRel')
    
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
    #Note this is called for record updates and new records inserts
    def save(self, *args, **kwargs):
        
        #If the obect primary keys is not null then we are updating an existing record
        #Check if we need to update sit logon details
        updateUserAccount = False
        if self.pk is not None:
            originalObject = guardian.objects.get(pk = self.pk)
            #Change account details if we have changed firstname and lastname
            if self.firstname != originalObject.firstname or self.lastname != originalObject.lastname:
                updateUserAccount = True   
                      
        
        
        # Set email text
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
        password = User.objects.make_random_password(length=8)
        body = body.format(name = self.firstname, username = username, password = password)     
        
        
        if self.email:        
            #If we are creating a new user send email with 
            if  updateUserAccount == False:        
                user              = User.objects.create_user(username, '', password) 
                user.is_staff = True
                user.save()
                self.userAccount  = user 
                # Call original save() method to do DB updates/inserts
                super(guardian, self).save(*args, **kwargs) 
                send_mail('Account Created', body, 'admin@BlackMountainScouts.com', [self.email])

            # If we are updating old account
            elif updateUserAccount == True:
                user             = originalObject.userAccount
                user.username    = username
                user.is_staff = True
                user.save()
                user.set_password (password)
                user.save()
                # Call original save() method to do DB updates/inserts
                super(guardian, self).save(*args, **kwargs) 
                send_mail('Account Updated', body, 'admin@BlackMountainScouts.com', [self.email])
                
        #If no email - do not try to send update/add email and change password to username         
        elif not self.email:
            #If we don't have an email change password from random generated to username
            password = username
            #If we are creating a new user send email with 
            if  updateUserAccount == False:       
                user = User.objects.create_user(username, '', password) 
                user.is_staff = True
                user.save()
                self.userAccount  = user 
                # Call original save() method to do DB updates/inserts
                super(guardian, self).save(*args, **kwargs) 
            # If we are updating old account
            elif updateUserAccount == True:
                user             = originalObject.userAccount
                user.username    = username
                user.set_password (password)
                user.is_staff = True
                user.save()
                # Call original save() method to do DB updates/inserts
                super(guardian, self).save(*args, **kwargs) 
            


           
            

            
                        
                
    
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)
    

                      




