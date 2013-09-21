from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()
from scoutsHerokuProject.whitelistAdmin import custom_discover

#List of apps to add to admin
whitelisted_apps = (
        'events',
        'members',
        'easy_maps',
    )
#Custom discovery function registers only selected apps in admin 
custom_discover (whitelisted_apps)


urlpatterns = patterns('',
   url(r'^$', 'scoutsHerokuProject.views.home'),                   
   url(r'^weblog/', include('zinnia.urls')),
   url(r'^comments/', include('django.contrib.comments.urls')),
   #Urls for login
   url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'scoutsHerokuProject/login.html'}),
   url(r'^accounts/logout/$', 'scoutsHerokuProject.views.logoutView'),

    # Examples:
    # url(r'^$', 'scoutsHerokuProject.views.home', name='home'),
    # url(r'^scoutsHerokuProject/', include('scoutsHerokuProject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)


