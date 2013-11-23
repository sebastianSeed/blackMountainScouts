from django.db import models
from django.core.validators import RegexValidator, validate_email
from django.contrib.auth.models import User
from django.core.mail import send_mail
from  django.contrib.auth.models import AbstractUser

#Includes for email format and send
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from  django.core.exceptions import ObjectDoesNotExist 

#Includes to get admin url for specific object
from django.core.urlresolvers import reverse



#Scout groups class and db table to allow users to set events per scout group
class scoutGroups(models.Model):
    name        = models.CharField(max_length=15,unique = True)
    description = models.CharField(max_length=150)
   
   #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.name)
    class Meta:
        verbose_name ="Scout Group"

        

## Abstract base clase for scouts - holds utility functions for logins and email creation
## Also holds common fields - DO NOT REMOVE fields as functions depend on these
class  allScoutUsers(models.Model):

    firstname = models.CharField(max_length=15)
    lastname  = models.CharField(max_length=15)
    email     = models.CharField(max_length=100, validators = [validate_email], blank = True)
    #TODO should phone be mandatory? I think so - users can also just enter 00000000
    phone = models.IntegerField(
                                    validators=[RegexValidator(
                                                            r'^[0-9]{8,12}',
                                                            'Phone numbers must be 8-12 digits.',
                                                            'Invalid Number'),
                                               ],) 
    
    
    userAccount  = models.OneToOneField(User)

    #Email parameters - these need to be overwritten in each class 
    #Templates for emails - can either write a whole bunch or use if statements to change wording both work -- if statements are cleaner
    addHtmlTemplate    =  'members/AddMemberEmail.html'
    addTxtTemplate     =  'members/addMemberEmail.txt'
    context         =  Context({'body':"Hey! You need to go into the allScoutUser model in members/models and make sure each child class overwrites this context variable!"})   

    class Meta:
        abstract = True
        #Records must have unique firstname and last name combo so we get unique usernames
        unique_together = ("firstname", "lastname")
    
        #Generate username and password from firstname_lastname
        # combination
    def createUserLogin(self,superUserFlag = False , accountActive = True):
        username = self.firstname +'_'+self.lastname
        username = username.lower()
        password = username.lower()
        ''' If user account already exists assume it's the same person and relink the account
        to guardian/ scout members/ scout leaders  account. We can safely assume this as database forces
        all firstname and lastname combination to be unique together'''
        try:
            user = User.objects.get(username = username )
        except  ObjectDoesNotExist:
            user = User.objects.create_user(username, '', password)          
                 
        if superUserFlag      == True:
            user.is_superuser = True
            user.is_staff     = True
            user.save()

        # If account is disabled then don't send an email.
        if accountActive   == False:
            user.is_active = False
            user.save()
            return user


        #If we have an email send update
        if self.email and accountActive:
            msg = self.createEmailMsg("User Account Created", self.addTxtTemplate, self.addHtmlTemplate, [ self.email], self.context)
            msg.send()
        return user                  

    def editUserLogin(self):
        user = self.userAccount
        #if user's first or last name has changed then we need to rename account
        newUserName  = self.firstname +'_'+self.lastname
        if newUserName != user.username:
            username = self.firstname +'_'+self.lastname
            username = username.lower()
            password = username.lower()
            #Update user details and save
            user.username    = username.lower()
            user.set_password (password)
            user.save()
            #If we have an email send update
            if self.email:
                msg = self.createEmailMsg("User Account Updated", self.addTxtTemplate, self.addHtmlTemplate, [ self.email], self.context)
                msg.send()
            return user

    # destination must be a tuple or list eg [myDestination@test.com , ]   or   [myDestination2@test.com , ]  
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
   
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)
    
    def getAdminUrl(self):        
        info = (self._meta.app_label, self._meta.module_name)
        admin_url = reverse('admin:%s_%s_change' % info, args=(self.pk,))
        return admin_url

    '''Clean up - remove user account when deleting a scout member / leader or guardian'''
    def delete(self, *args, **kwargs):
        if self.pk:   
            self.userAccount.delete()
            super(allScoutUsers, self).delete(*args, **kwargs)  
        

class scoutMember(allScoutUsers):
    preferredName = models.CharField(max_length=15)    
    dob           = models.DateField(verbose_name='Date of Birth')
    birthCountry  = models.CharField(max_length=15,verbose_name='Country of Birth')   
    nationality   = models.CharField(max_length=15,verbose_name='Nationality') 
    religion      = models.CharField(max_length=15,verbose_name='Religion') 
    lote          = models.CharField(max_length=15,verbose_name='Languages other then English spoken at home?') 
    indigenous    = models.BooleanField(verbose_name='Of Aboriginal or Torres Strait Island descent?')
    addressHome   = models.CharField(max_length=100,verbose_name='Home Address') 
    postCodeHome  = models.IntegerField(
                                            validators=[RegexValidator(
                                                                    r'^[0-9]{4}',
                                                                    'Post code must be 4 digits and can not start with 0.',
                                                                    'Invalid post code'),
                                                       ], 
                                           verbose_name='Post code',
                                       ) 
    indigenous    = models.BooleanField()
     
    

    
    
    
    parents       = models.ManyToManyField('guardian', related_name = 'scoutmember_guardians')
    scoutGroup    = models.ForeignKey(scoutGroups , verbose_name="Scout group") 
    
     
    def save(self, *args, **kwargs):                
        #Create disabled accoutn for each scout member, leaving this here until client confirms if members should have logons.
        if self.pk:
            self.userAccount = self.editUserLogin()
        else:
            self.userAccount = self.createUserLogin()
        super(scoutMember, self).save(*args, **kwargs) 
        

        
class scoutLeader(allScoutUsers):
    def save(self, *args, **kwargs):                 
        #updating an existing record
        if self.pk:
            self.userAccount = self.editUserLogin()
        #creating new record
        else:
            self.userAccount = self.createUserLogin(True)
                             
        # Call original save() method to do DB updates/inserts
        super(scoutLeader, self).save(*args, **kwargs) 
        
        


class guardian(allScoutUsers):
    addressHome     = models.CharField(max_length=100,verbose_name='Home Address') 
    postCodeHome    = models.IntegerField(
                                        validators=[RegexValidator(
                                                                r'^[0-9]{4}',
                                                                            'Post code must be 4 digits and can not start with 0.'
                                                                'Invalid post code'),
                                                   ], 
                                       verbose_name='Post code',
                                   ) 
    addressPostal   = models.CharField(max_length=100,verbose_name='Postal Address', blank = True , ) 
    postCodePostal  = models.IntegerField(
                                            validators=[RegexValidator(
                                                                    r'^[0-9]{4}',
                                                                     'Post code must be 4 digits and can not start with 0.',
                                                                    'Invalid post code'),
                                                       ], 
                                           verbose_name='Post code',
                                            blank = True , null = True , 
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
                                                   verbose_name = "Work phone", 
                                                    blank = True , null = True,) 
    mobilePhone = models.IntegerField(
                                        validators=[RegexValidator(
                                                                r'^[0-9]{8,12}',
                                                                'Phone numbers must be 8-12 digits.',
                                                                'Invalid Number'),
                                                   ],
                                                   verbose_name = "Mobile", 
                                                    blank = True , null = True,) 
    
    
    


    #Function to determine if deleting parent would result in scout member on system without any parent     
    def deleteWillOrphanChild(self):
        if self.pk:   
            relatedScouts          = self.scoutmember_guardians.all()      
            for scout in relatedScouts:
                #Scout has more then one guardian on system - delete will not orphan them, continue
                if scout.parents.count() >  1:
                    return False
                else:
                    return True
                 
                 
                
    def save(self, *args, **kwargs):        
        
        #updating an existing record
        if self.pk:
            self.userAccount = self.editUserLogin()
        #creating new entry
        else:
            self.userAccount = self.createUserLogin(False)
                   
        # Call original save() method to do DB updates/inserts
        super(guardian, self).save(*args, **kwargs) 

    
        
    def delete(self, *args, **kwargs):
        if self.pk:   
            bDeleteWillOrphanChild = self.deleteWillOrphanChild() 
            #If deleting will orphan child do not delete
            if bDeleteWillOrphanChild:
                pass
            else:
                super(guardian, self).delete(*args, **kwargs) 

                
                



