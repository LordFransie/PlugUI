from django.conf.urls.defaults import *
from django.conf import settings

urlpatterns = patterns('',
	(r'^$', 'home.views.index', {}, 'home'),
)
