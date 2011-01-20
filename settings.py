# Django settings for PlugUI project.
DEBUG = True
TEMPLATE_DEBUG = DEBUG
STATIC_DOC_ROOT = '/opt/PlugUI/static'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '/var/lib/PlugUI/db.sqlite3',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

TIME_ZONE = 'None'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = False
USE_L10N = False
MEDIA_ROOT = ''
MEDIA_URL = ''
LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/home/'
ADMIN_MEDIA_PREFIX = '/media/'

# how to handle this during deployment?
SECRET_KEY = '@0axld1dwh$9sjyb#_na+u#z7_wf(*^z7)qp)52a(wb*79@-v8'

# List of callables that know how to import templates from various sources.
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
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    '/opt/PlugUI/views'
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.request',
)

INSTALLED_APPS = (
    'django.contrib.admin',	
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'users',
    'privateapi',
    'system',
    'files',
    'apps',
    'home',
    'cpserver',
)
