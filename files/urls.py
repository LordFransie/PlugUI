from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import redirect_to


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^browse', 'files.views.browse', {}, 'browse'),
	(r'^shares', 'files.views.shares', {}, 'shares'),
	(r'^addshare', 'files.views.addshare', {}, 'addshare'),
	(r'^deleteshare', 'files.views.deleteshare', {}, 'deleteshare'),
	(r'^download/(?P<shareuuid>\w+)', 'files.views.downloadshare', {}, 'downloadshare'),
	(r'^$', redirect_to, {'url': '/files/browse'}),
)
