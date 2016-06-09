# Django settings for scoutsHerokuProject project.
import os 



#Production settings for email and file storages
# Depends on being run in heroku with environment variables set correctly
EMAIL_HOST_USER = os.environ['SENDGRID_USERNAME']
EMAIL_HOST= 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = os.environ['SENDGRID_PASSWORD']
DEFAULT_FROM_EMAIL = 'donotreply@BlackMountainScouts.com'

#New AMAZON S3 Settings -- Harcoded for 1st test
AWS_STORAGE_BUCKET_NAME = 'blackmountainstorage'
AWS_ACCESS_KEY_ID =  os.environ['AWS_SECRET_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

# Tell django-storages that when coming up with the URL for an item in S3 storage, keep
# it simple - just use this domain plus the path. (If this isn't set, things get complicated).
# This controls how the `static` template tag from `staticfiles` gets expanded, if you're using it.
# We also use it in the next setting.
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

STATICFILES_LOCATION = 'static'
STATICFILES_STORAGE = 'scoutsHerokuProject.customStorages.StaticStorage'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION)


MEDIAFILES_LOCATION = 'media'
MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
DEFAULT_FILE_STORAGE = 'scoutsHerokuProject.customStorages.MediaStorage'


#Contact form categories for message
ENVELOPE_CONTACT_CHOICES = (
    ('',    u"Choose"),
    (10,    u"General question"),
    (None,   u"Other"),
)

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
        'NAME':    os.path.join(PROJECT_PATH, 'guides.db'),  # Or path to database file if using sqlite3.
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


TIME_ZONE = 'Australia/Sydney'
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


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
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

# Middleware for various tasks including forcing user logon

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'scoutsHerokuProject.middleware.LoginRequiredMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


# Pages that are viewable by public / do not require login
LOGIN_EXEMPT_URLS = (    '^$',           
   '^accounts/login/',
   '^contactForm/',
   '^forms/',
   '^about/',
   )


ROOT_URLCONF = 'scoutsHerokuProject.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'scoutsHerokuProject.wsgi.application'


# Settings for map application starting location , this is used when recording events 
# and on the about us page
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
    #  Apps created for this site
    'slideShow',
    'events',
    'members',
    'newsletter',
    'guideForms',
    # Third party applications
    # including Dependencies for events , members and newsletters
    'django.contrib.comments',
    'tagging',
    'mptt',
    'easy_maps',
    #Amazon S3 File storage backend for storing newsletters and photos
    'storages',
    #Amazon S3 plugin to support seperate media and static folders
    's3_folder_storage',
    'envelope',
    'django_tables2',
    #Gallery add on
    'photologue',
     'south',
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



# 


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







# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Hosts/domain names that are valid for this site; required if DEBUG is False
# Allow all host headers
ALLOWED_HOSTS = ['*']

# from SettingUtils import getScoutLeaders
# ENVELOPE_EMAIL_RECIPIENTS = getScoutLeaders()
# ENVELOPE_MESSAGE_THANKS   = 'Message has been sent successfuly.'
# ENVELOPE_MESSAGE_ERROR    = 'Error - Form has not been submitted please try again later' 

LOGOUT_URL ='/'  
  
######################
#####   SETTINGS THAT MAY NOT BE REQUIRED  - requires test
####
##########################

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)


TEMPLATE_DIRS = (
                 os.path.join(PROJECT_PATH, 'templates')
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
 )