from django.conf.urls import patterns, include, url
from django.contrib import admin
from girlGuidesProject.SettingUtils import custom_discover
from django.conf import settings

#admin.autodiscover()
#List of apps to add to admin
whitelisted_apps = (
        'girlGuidesProject.events',
        'girlGuidesProject.members',
        'easy_maps',
        'girlGuidesProject',
        'girlGuidesProject.slideShow',
        'girlGuidesProject.newsletter',
        'girlGuidesProject.guideForms',
        'photologue',
    )
# #Custom discovery function registers only selected apps in admin 
custom_discover (whitelisted_apps)

urlpatterns = patterns('',
   url(r'^$', 'girlGuidesProject.views.home'),                   
   #Urls for login
   url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}),
   url(r'^accounts/logout/$', 'girlGuidesProject.views.logoutView'),
   url(r'^contactForm/',    include('envelope.urls')),
   url(r'^events/$',  'girlGuidesProject.events.views.eventList'  ),
   url(r'^events/id=(?P<id>\d{1,10})/$', 'girlGuidesProject.events.views.eventDetail', name = 'eventMap'),
   url(r'^newsletters/$',  'girlGuidesProject.newsletter.views.newsletterList'  ),
   url(r'^forms/$',  'girlGuidesProject.guideForms.views.formList'  ),
   url(r'^photologue/', include('photologue.urls')),

   url(r'^photologue/', include('photologue.urls')),

#    url(r'^newsletters/id=(?P<id>\d{1,4})$', 'newsletter.views.newsletterDetail'),

   url(r'^about/$',  'girlGuidesProject.views.aboutView' ),

   # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )