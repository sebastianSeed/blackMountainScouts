'''
Created on 07/09/2013

@author: sebastian
'''

# from zinnia.models.entry import EntryAbstractClass
# 
# from django.core.mail import send_mail
# 
# class ZinniaCustomEntry(EntryAbstractClass):
# 
#     def save(self, *args, **kwargs):     
#         super(ZinniaCustomEntry, self).save(*args, **kwargs) # Call the "real" save() method.
#         print ' hello world'
#         
#     class Meta(EntryAbstractClass.Meta):
#         abstract = True
#        # TODO READ DOCO AND EXTEND THIS TO SEND EMAIL WHENEVER WE SAVE AN ENTRY