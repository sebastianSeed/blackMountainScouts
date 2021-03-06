from django.conf.urls import patterns, include, url
from django.contrib import admin
from scoutsHerokuProject.SettingUtils import custom_discover
from django.conf import settings


#List of apps to add to admin
whitelisted_apps = (
        'events',
        'members',
        'easy_maps',
        'scoutsHerokuProject',
        'slideShow',
        'newsletter',
        'guideForms',
        'photologue',
    )
# #Custom discovery function registers only selected apps in admin 
custom_discover (whitelisted_apps)

urlpatterns = patterns('',
   url(r'^$', 'scoutsHerokuProject.views.home'),                   
   #Urls for login
   url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'main/login.html'}),
   url(r'^accounts/logout/$', 'scoutsHerokuProject.views.logoutView'),
   url(r'^contactForm/',    include('envelope.urls')),
   url(r'^events/$',  'events.views.eventList'  ),
   url(r'^events/id=(?P<id>\d{1,10})/$', 'events.views.eventDetail', name = 'eventMap'),
   url(r'^newsletters/$',  'newsletter.views.newsletterList'  ),
   url(r'^forms/$',  'guideForms.views.formList'  ),
   url(r'^photologue/', include('photologue.urls')),

   url(r'^photologue/', include('photologue.urls')),

#    url(r'^newsletters/id=(?P<id>\d{1,4})$', 'newsletter.views.newsletterDetail'),

   url(r'^about/$',  'scoutsHerokuProject.views.aboutView' ),

   # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
        (r'media/(?P<path>.*)', 'serve', {'document_root': settings.MEDIA_ROOT}),
    )