# This module is available as common_settings from projects' settings module.
# It contains settings used in all projects.

import os.path
from django.conf import global_settings

KIT_ROOT=os.path.realpath(os.path.join(os.path.dirname(__file__), ".."))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(KIT_ROOT, 'crowdsense.db')  # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/London'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-gb'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    #ab 'ab.loaders.load_template_source',
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django_authopenid.middleware.OpenIDMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #ab 'ab.middleware.ABMiddleware',
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    # builtin
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    # third-party
    #ab 'ab',
    'ajax_validation',
    'compress',
    'debug_toolbar',
    'contact_form',
    'django_authopenid',
    'django_evolution',
    'django_extensions',
    'django_pipes',
    'filter',
    'mailer',
    'mptt',
    'notification',
    'pages',
    'paypal.standard.ipn',
    'perfect404',
    'piston',
    'profiles',
    'registration',
    'rosetta',
    'tagging',
    'uni_form',
    # own
    'mashup.pipeadmin',
    'muaccounts',
    'prepaid',
    'quotas',
    'subscription',
    # local
    'crowdsense',
)

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'django_authopenid.context_processors.authopenid',
    'pages.context_processors.media',
    )

TEMPLATE_DIRS = ( os.path.join(KIT_ROOT, 'templates'), )

INTERNAL_IPS = ( '127.0.0.1', )

AUTH_PROFILE_MODULE = 'crowdsense.UserProfile'

COMPRESS = True
COMPRESS_VERSION = True

_default_css_files = ('yui-app-theme/yuiapp.css',
                      'authopenid/css/openid.css',
                      'uni_form/uni-form-generic.css',
                      'uni_form/uni-form.css',
                      )

COMPRESS_CSS = {                        # different themes for MUAs
    'all' : {
        'name' : 'Default theme',
        'source_filenames' : _default_css_files,
        'output_filename' : 'style.css'},
    }
COMPRESS_JS = {
    'all' : {
        'source_filenames' : ('authopenid/js/jquery-1.3.2.min.js',
                              'uni_form/uni-form.jquery.js',
                              ),
        'output_filename' : 'scripts.js'},
    }

PAGE_TAGGING = True
PAGE_TINYMCE = False
PAGE_USE_SITE_ID = True
PAGE_LANGUAGES = (
    ('en-gb', 'English'),
)
PAGE_UNIQUE_SLUG_REQUIRED = True
DEFAULT_PAGE_TEMPLATE = 'page.html'
PAGE_TEMPLATES = (
    ('page-templates/single-body.html', 'Single body'),
    ('page-templates/before-and-after.html', 'Content before and after dynamic content'),
)


PAYPAL_TEST = True
PAYPAL_RECEIVER_EMAIL='example@example.com'
ACCOUNT_ACTIVATION_DAYS=7
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/signin/'
SUBSCRIPTION_PAYPAL_SETTINGS = {
    'business' : PAYPAL_RECEIVER_EMAIL,
    }

MUACCOUNTS_ROOT_DOMAIN = 'example.com'
# MUACCOUNTS_DEFAULT_DOMAIN = 'www.example.com'
MUACCOUNTS_DEFAULT_URL = 'http://www.example.com:8001/'
MUACCOUNTS_PORT=8000
MUACCOUNTS_IP = '127.0.0.1'
MUACCOUNTS_THEMES = [('all','Default')]

# Calculate themes together with compress CSS sets.
for theme in ('Aqua', 'Green', 'Purple', 'Red', 'Tan Blue',):
    codename = theme.lower().replace(' ','_')

    MUACCOUNTS_THEMES.append( (codename,theme) )
    COMPRESS_CSS[codename] = {
        'source_filenames' : ( _default_css_files[:1]
                               + ('yui-app-theme/%s.css'%codename,)
                               + _default_css_files[1:] ),
        'output_filename' : 'style.%s.css' % codename,
        }
