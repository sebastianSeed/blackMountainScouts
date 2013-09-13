from django.db import models
from django.core.validators import RegexValidator
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

    
    def __unicode__(self):
        return u'%s %s' % (self.firstname, self.lastname)
    

                      




