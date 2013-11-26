# Django settings for scoutsHerokuProject project.
import os 


if 'ONHEROKU' in os.environ:
    DEBUG = False
    ##Setup SENDGRID email add on for heroku
    EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
    EMAIL_HOST= 'smtp.sendgrid.net'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
    DEFAULT_FROM_EMAIL = 'donotreply@BlackMountainScouts.com'
    #AMAZON S3 SETTINGS
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_ACCESS_KEY_ID = os.environ['AWS_SECRET_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = "media"
    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    STATIC_S3_PATH = "static"
    MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
   # MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
    MEDIA_URL = '//blackmountainstorage.s3.amazonaws.com/media/'
    STATIC_ROOT = "/%s/" % STATIC_S3_PATH
    STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

#Local development settings  
else:
    DEBUG = True
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    STATIC_URL = '/static/'    
    MEDIA_URL = '/media/'



#DJANGO Suit Admin theme configuration
SUIT_CONFIG = {
    'ADMIN_NAME': 'Black Mountain Girl Guides',
       'SEARCH_URL': ''
}

ADMINS = (
     ('seb', 'sebas.home1@gmail.com'),
)

MANAGERS = ADMINS

PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


# Place holder for local DB to keep django happy
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME':    os.path.join(PROJECT_PATH, 'scouts.db'),  # Or path to database file if using sqlite3.
        # The following settings are not used with sqlite3:
        'USER': '',
        'PASSWORD': '',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

# If we are on heroku then this url will reflect path to heroku db 
#Otherwise it will default to local system - will need to change per dev enviroment - path must exist
import dj_database_url
DATABASES['default'] =  dj_database_url.config(default='sqlite:///'+os.path.join(PROJECT_PATH, 'scouts.db'))


#Redirect to home page / Index page after login
LOGIN_REDIRECT_URL = '/'
#Note you can't use reverse url lookup here as settings is loaded before URLs

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = ''



# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gmn#gg)y!&u_je&$e#@sp&+ik!+v@+hwnv%wkoga^5^jw*&vlf'

# List of callables that know how to import templates from various sources.
#Check template_dir first
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)



ROOT_URLCONF = 'scoutsHerokuProject.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'scoutsHerokuProject.wsgi.application'


EASY_MAPS_CENTER = (-41.3, 32)



INSTALLED_APPS = (
#Suit is modern admin theme
    'suit',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'events',
    'members',
    'newsletter',
    # Dependencies for events , members and newsletters
    'django.contrib.comments',
    'tagging',
    'mptt',
    'easy_maps',
    #Amazon S3 File storage backend for storing newsletters and photos
    'storages',
    #Amazon S3 plugin to support seperate media and static folders
    's3_folder_storage',
    'envelope',
    'gallery',
    'django_tables2',
    #'django_google_maps',

 
)

# 1st entry is Suit admin theme config

TEMPLATE_CONTEXT_PROCESSORS = (
   'django.core.context_processors.request',
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'django.core.context_processors.media',
  'django.core.context_processors.static',
  'django.contrib.messages.context_processors.messages',

  ) # Optional







STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)


# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}




TEMPLATE_DIRS = (
                 os.path.join(PROJECT_PATH, 'templates')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)



# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
# Allow all host headers
ALLOWED_HOSTS = ['*']

#from SettingUtils import getScoutLeaders
ENVELOPE_EMAIL_RECIPIENTS = ['stephy123123@gmail.com',]
ENVELOPE_MESSAGE_THANKS   = 'Message has been sent successfuly , a scout leader will be in contact with you shortly.'
ENVELOPE_MESSAGE_ERROR    = 'Error - Form has not been submitted please try again later' 

  
  
if DEBUG:
     INTERNAL_IPS = ('127.0.0.1',)
     MIDDLEWARE_CLASSES += (
         'debug_toolbar.middleware.DebugToolbarMiddleware',
     )
 
     INSTALLED_APPS += (
         'debug_toolbar',
     )
 
     DEBUG_TOOLBAR_PANELS = (
         'debug_toolbar.panels.version.VersionDebugPanel',
         'debug_toolbar.panels.timer.TimerDebugPanel',
         'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
         'debug_toolbar.panels.headers.HeaderDebugPanel',
         'debug_toolbar.panels.profiling.ProfilingDebugPanel',
         'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
         'debug_toolbar.panels.sql.SQLDebugPanel',
         'debug_toolbar.panels.template.TemplateDebugPanel',
         'debug_toolbar.panels.cache.CacheDebugPanel',
         'debug_toolbar.panels.signals.SignalDebugPanel',
         'debug_toolbar.panels.logger.LoggingPanel',
     )
 
     DEBUG_TOOLBAR_CONFIG = {
         'INTERCEPT_REDIRECTS': False,
     }

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
 
    INSTALLED_APPS += (
        'debug_toolbar',
    )
 
    DEBUG_TOOLBAR_PANELS = (
        'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        #'debug_toolbar.panels.profiling.ProfilingDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.signals.SignalDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
 
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
    }
