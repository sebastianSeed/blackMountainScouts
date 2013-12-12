from django.db import models


 

 
class GuideForms(models.Model):
    title                      = models.CharField(max_length=150) 
    form                       = models.FileField(upload_to = "forms" )

        
    #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.title)
 
    class Meta:
        verbose_name ="Form"
             
