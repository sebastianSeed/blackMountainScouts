from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


#Scout groups class and db table to allow users to set events per scout group
class Gallery(models.Model):
    description = models.CharField(max_length=150) 
    image       = models.ImageField(upload_to = "gallery")
    public      = models.BooleanField(help_text = "Display this image on home page slideshow")
    #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.description)
    class Meta:
        verbose_name ="Image"
        

class Newsletter(models.Model):
    title            = models.CharField(max_length=150) 
    date             = models.DateField(auto_now=False)
    newsletter       = models.FileField(upload_to = "newsletter" )
    #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.title)

    class Meta:
        verbose_name ="Newsletter"
            
        
    def clean(self):
        if not str(self.newsletter).endswith('.pdf'):
            raise ValidationError(u'File must be a pdf')
        super(Newsletter, self).clean()  
