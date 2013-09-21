from django.db import models
from django.core.validators import RegexValidator, validate_email
from django.contrib.auth.models import User
from django.core.mail import send_mail
from  django.contrib.auth.models import AbstractUser

#Includes for email format and send
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context

#Scout groups class and db table to allow users to set events per scout group
class scoutGroups(models.Model):
    name        = models.CharField(max_length=15)
    description = models.CharField(max_length=150)
   
   #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.name)
    
## Abstract base clase for scouts - holds utility functions for logins and email creation
## Also holds common fields - DO NOT REMOVE fields as functions depend on these
class  allScoutUsers(models.Model):

    firstname = models.CharField(max_length=15)
    lastname  = models.CharField(max_length=15)
    email      = models.CharField(max_length=100, validators = [validate_email], blank = True)
    #TODO should phone be mandatory? I think so - users can also just enter 00000000
    phone = models.IntegerField(
                                    validators=[RegexValidator(
                                                            r'^[0-9]{8,12}',
                                                            'Phone numbers must be 8-12 digits.',
                                                            'Invalid Number'),
                                               ],) 
    
    
    #Everyone gets a login on website - we simply hide this field in admin and generate it here
    userAccount  = models.OneToOneField(User)

    #Email parameters - these need to be overwritten in each class 
    #Templates for emails - can either write a whole bunch or use if statements to change wording both work -- if statements are cleaner
    addHtmlTemplate    =  'members/AddMemberEmail.html'
    addTxtTemplate     =  'members/addMemberEmail.txt'
    context         =  Context({'body':"Hey! You need to go into the allScoutUser model in members/models and make sure each child class overwrites this context variable!"})   

    #Meta attributes for django
    class Meta:
        abstract = True
        #Records must have unique firstname and last name combo so we get unique usernames
        unique_together = ("firstname", "lastname")
    
    #Create user login - split out as used by scout admin , parents and children
    def createUserLogin(self,superUserFlag = False ):
        #Generate username and password for email and account update/creation
        username = self.firstname +'_'+self.lastname
        username = username.lower()
        password = username.lower()
        user = User.objects.create_user(username, '', password)     
        if superUserFlag == True:
            user.is_superuser = True
            user.is_staff     = True

        user.save()

        #If we have an email send update
        if self.email:
            msg = self.createEmailMsg("User Account Created", self.addHtmlTemplate, self.addTxtTemplate, [ self.email], self.context)
            msg.send()
        return user                  

    def editUserLogin(self):
        #User account is not updated until save completes - need to call this function before saving to db
        user = self.userAccount
        #if user's first or last name has changed then we need to rename account
        if self.firstname != user.firstname or self.lastname != user.lastname:
            username = self.firstname +'_'+self.lastname
            username = username.lower()
            password = username.lower()
            #Update user details and save
            user.username    = username.lower()
            user.set_password (password)
            user.save()
            #If we have an email send update
            if self.email:
                msg = self.createEmailMsg("User Account Updated", self.txtTemplate, self.htmlTemplate, [ self.email], self.context)
                msg.send()
            return user

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
   
   #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)

class scoutMember(allScoutUsers):
    preferredName = models.CharField(max_length=15)    
    dob           = models.DateField(verbose_name='Date of Birth')
    birthCountry  = models.CharField(max_length=15,verbose_name='Country of Birth')   
    nationality   = models.CharField(max_length=15,verbose_name='Nationality') 
    religion      = models.CharField(max_length=15,verbose_name='Religion') 
    lote          = models.CharField(max_length=15,verbose_name='Languages other then English spoken at home?') 
    indigenous    = models.BooleanField(verbose_name='Of Aboriginal or Torres Strait Island descent?')
    addressHome   = models.CharField(max_length=100,verbose_name='Home Address') 
    postCodeHome = models.IntegerField(
                                            validators=[RegexValidator(
                                                                    r'^[0-9]{4}',
                                                                    'Post code must be 4 digits.',
                                                                    'Invalid post code'),
                                                       ], 
                                           verbose_name='Post code',
                                       ) 
    indigenous    = models.BooleanField()
     
    

    
    
    
    parents       = models.ManyToManyField('guardian', related_name = 'scoutmember_guardians')
    scoutGroup    = models.ForeignKey(scoutGroups , verbose_name="Scout group") 
    

    class meta:
        unique_together = ("firstname", "lastname")
      
   #Note this is called for record updates and new records inserts 
    def save(self, *args, **kwargs):        
         
        #If the obect primary keys is not null then we are updating an existing record
        if self.pk is not None:
            self.userAccount = self.editUserLogin()
        #If not self.pk - we are creating new entry
        else:
            self.userAccount = self.createUserLogin(False)
                   
        # Call original save() method to do DB updates/inserts
        super(scoutMember, self).save(*args, **kwargs) 
    
class scoutLeader(allScoutUsers):

   #Note this is called for record updates and new records inserts 
    def save(self, *args, **kwargs):        
         
        #If the obect primary keys is not null then we are updating an existing record
        if self.pk is not None:
            self.userAccount = self.editUserLogin()

        #If not self.pk - we are creating new entry
        else:
            self.userAccount = self.createUserLogin(True)
                   
        # Call original save() method to do DB updates/inserts
        super(scoutLeader, self).save(*args, **kwargs) 


class guardian(allScoutUsers):
    addressHome     = models.CharField(max_length=100,verbose_name='Home Address') 
    postCodeHome = models.IntegerField(
                                        validators=[RegexValidator(
                                                                r'^[0-9]{4}',
                                                                'Post code must be 4 digits.',
                                                                'Invalid post code'),
                                                   ], 
                                       verbose_name='Post code',
                                   ) 
    addressPostal   = models.CharField(max_length=100,verbose_name='Postal Address') 
    postCodePostal  = models.IntegerField(
                                            validators=[RegexValidator(
                                                                    r'^[0-9]{4}',
                                                                    'Post code must be 4 digits.',
                                                                    'Invalid post code'),
                                                       ], 
                                           verbose_name='Post code',
                                         ) 
    homePhone = models.IntegerField(
                                            validators=[RegexValidator(
                                                                    r'^[0-9]{8,12}',
                                                                    'Phone numbers must be 8-12 digits.',
                                                                    'Invalid Number'),
                                                       ],
                                                       verbose_name = "Home phone", ) 
    workPhone = models.IntegerField(
                                        validators=[RegexValidator(
                                                                r'^[0-9]{8,12}',
                                                                'Phone numbers must be 8-12 digits.',
                                                                'Invalid Number'),
                                                   ],
                                                   verbose_name = "Work phone", ) 
    mobilePhone = models.IntegerField(
                                        validators=[RegexValidator(
                                                                r'^[0-9]{8,12}',
                                                                'Phone numbers must be 8-12 digits.',
                                                                'Invalid Number'),
                                                   ],
                                                   verbose_name = "Mobile", ) 
    
    
    

    #TODO If parent is last guardian for a scout then raise message and delete scout if confirmed
    ## CHECK OUT http://stackoverflow.com/questions/1471909/django-model-delete-not-triggered       
                 
   #Note this is called for record updates and new records inserts 
    def save(self, *args, **kwargs):        
         
        #If the obect primary keys is not null then we are updating an existing record
        if self.pk is not None:
            self.userAccount = self.editUserLogin()
        #If not self.pk - we are creating new entry
        else:
            self.userAccount = self.createUserLogin(False)
                   
        # Call original save() method to do DB updates/inserts
        super(guardian, self).save(*args, **kwargs) 



