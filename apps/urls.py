from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to


urlpatterns = patterns('',
	(r'^samba', 'apps.views.samba', {}, 'samba'),
	(r'^minidlna', 'apps.views.minidlna', {}, 'minidlna'),
	(r'^about', 'apps.views.index', {}, 'apps'),
	(r'^$', redirect_to, {'url': '/apps/about'}),
)
