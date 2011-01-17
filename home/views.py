from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth.decorators import login_required

from system.models import SystemStats
from home.models import PlugappsNewsEntry

@login_required
def index(request):
	news_list = PlugappsNewsEntry.objects.all()
	systemstats = SystemStats()
	updatecount = systemstats.updatecount
	updatesavailable = systemstats.updatesavailable
	return render_to_response('home.html', {"updatecount": updatecount, "updatesavailable": updatesavailable, "news_list": news_list }, context_instance=RequestContext(request))
