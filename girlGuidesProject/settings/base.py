# Django settings for girlGuidesProject project.
import os
import dj_database_url

#Settings path is the current settings folder e.g. /mnt/project/girlGuidesProject/settings
SETTINGS_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = (os.path.split(SETTINGS_PATH))[0]

STATICFILES_LOCATION = 'static'
STATIC_URL = '/static/'
# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

MEDIAFILES_LOCATION = 'media'
STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)


TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, 'templates')
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)


#Contact form categories for message
ENVELOPE_CONTACT_CHOICES = (
    ('', u"Choose"),
    (10, u"General question"),
    (None, u"Other"),
)

#DJANGO Suit Admin theme configuration
SUIT_CONFIG = {
    'ADMIN_NAME': 'Black Mountain Girl Guides',
    'SEARCH_URL': ''
}

ADMINS = (
    ('Sebastian', 'sebas.home1@gmail.com'),
    ('Paul', 'mrpaultruong@gmail.com'),
)

MANAGERS = ADMINS

LOGIN_REDIRECT_URL = '/'
#Note you can't use reverse url lookup here as settings is loaded before URLs

#Timezone settings , see Django doc for details
TIME_ZONE = 'Australia/Sydney'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gmn#gg)y!&u_je&$e#@sp&+ik!+v@+hwnv%wkoga^5^jw*&vlf'

# List of callables that know how to import templates from various sources.
#Check template_dir first
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

    #'django.template.loaders.eggs.Loader',
)

# Middleware for various tasks including forcing user logon

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'girlGuidesProject.middleware.LoginRequiredMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Pages that are viewable by public / do not require login
LOGIN_EXEMPT_URLS = ('^$',
                     '^accounts/login/',
                     '^contactForm/',
                     '^forms/',
                     '^about/',
                    )

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'girlGuidesProject.wsgi.application'

ROOT_URLCONF = 'girlGuidesProject.urls'

# Settings for map application starting location , this is used when recording events and on the about us page
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
    'girlGuidesProject.slideShow',
    'girlGuidesProject.events',
    'girlGuidesProject.members',
    'girlGuidesProject.newsletter',
    'girlGuidesProject.guideForms',
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

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Hosts/domain names that are valid for this site; required if DEBUG is False
# Allow all host headers
ALLOWED_HOSTS = ['*']

# from SettingUtils import getScoutLeaders
# ENVELOPE_EMAIL_RECIPIENTS = getScoutLeaders()
# ENVELOPE_MESSAGE_THANKS   = 'Message has been sent successfuly.'
# ENVELOPE_MESSAGE_ERROR    = 'Error - Form has not been submitted please
# try again later'
LOGOUT_URL = '/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, '../static'),
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, '../templates/'),
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)