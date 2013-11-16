from django.db import models

# Create your models here.


#Scout groups class and db table to allow users to set events per scout group
class gallery(models.Model):
    description = models.CharField(max_length=150) 
    image       = models.ImageField(upload_to = "gallery")
    #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.description)
    class Meta:
        verbose_name ="Image"
        

class newsletter(models.Model):
    title            = models.CharField(max_length=150) 
    date             = models.DateField(auto_now=False)
    newsletter       = models.FileField(upload_to = "newsletter")
    #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.description)
    class Meta:
        verbose_name ="Newsletter"
        

