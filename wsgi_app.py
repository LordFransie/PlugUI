import uwsgi
import sys
import os

# insert the parent path to ensure settings file is loaded
sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), '../'))
os.environ['DJANGO_SETTINGS_MODULE'] = '%s.settings' % os.path.abspath(os.path.dirname(__file__)).split('/')[-1]

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
uwsgi.applications = { '' : application }

