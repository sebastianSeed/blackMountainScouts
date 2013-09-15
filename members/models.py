from django.db import models
from django.core.validators import RegexValidator, validate_email
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your models here.

#TODO MODEL FOR ADMINS? Extend users + give them rights to edit everything -- eg forum newsletters etc
class scoutMember(models.Model):
    firstname = models.CharField(max_length=30)
    lastname  = models.CharField(max_length=100)
    dob       = models.DateField(verbose_name='birthday')
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)




class guardian(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=100)
    phone = models.IntegerField(
                                            validators=[RegexValidator(
                                                                    r'^[0-9]{8,12}',
                                                                    'Phone numbers must be 8-12 digits.',
                                                                    'Invalid Number'),
                                                       ],) 
    kids = models.ManyToManyField('scoutMember')
#    kids  = models.ForeignKey('scoutMember')
    email = models.CharField(max_length=100, validators = [validate_email], blank = True)
    
    def save(self, *args, **kwargs):
        super(guardian, self).save(*args, **kwargs) # Call the "real" save() method.
        username = self.firstname +'_'+self.lastname
        password = User.objects.make_random_password(length=8)
        user = User.objects.create_user(username, '', password)
                
        #If an email exists for user send account confirmation email
        if self.email:
            self.password = 'dummyPassword'
            body = """
            Your user account has been updated or created,
            Username:%(username)s
            Password:%(password)s 
            You can use these details to logon onto the scout's website.
            Thank you 
            """
            body.format((self.user.username), password)
            send_mail('Account Updated or Added', body, 'admin@BlackMountainScouts.com', [self.email])

            
            
    
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)
    

                      




