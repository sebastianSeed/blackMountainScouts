from django.db import models

# Create your models here.
class Gallery(models.Model):
    description = models.CharField(max_length=150) 
    image       = models.ImageField(upload_to = "gallery")
    public      = models.BooleanField(help_text = "Display this image on home page slideshow")
    #Function that defines how object shows up in admin ie the name 
    def __unicode__(self):
        return u'%s' % (self.description)
    class Meta:
        verbose_name ="Image"
         