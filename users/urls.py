from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
	(r'^create$', 'users.views.create', {}, 'createuser'),
	(r'^delete$', 'users.views.delete', {}, 'deleteuser'),
	(r'^show', 'users.views.index', {}, 'users'),
	(r'^login', 'django.contrib.auth.views.login', {'template_name': 'users/login.html'}, 'login'),
	(r'^logout', 'django.contrib.auth.views.logout', {'template_name': 'users/logout.html'}, 'logout'),
	(r'^$', redirect_to, {'url': '/users/show'}),
)
