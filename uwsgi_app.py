import os
import sys
sys.path.append("/opt/PlugUI")
os.environ['DJANGO_SETTINGS_MODULE'] = 'PlugUI.settings'
import uwsgi
import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
uwsgi.applications = {'':application}
