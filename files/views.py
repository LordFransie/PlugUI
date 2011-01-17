from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from files.models import ShareForm
from files.models import Share
from django.core.files.storage import Storage
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.core.servers.basehttp import FileWrapper
from django.views.decorators.http import condition
import privateapi.core

import uuid, urllib, base64, sys, traceback, mimetypes, os

class PlugStorage(Storage):
	def __init__(self, option=None):
		if not option:
			option = settings.CUSTOM_STORAGE_OPTIONS
			
	def delete():
		pass
		
	def exists():
		pass
		
	def listdir():
		pass
	
	def size():
		pass
		
	def url():
		pass
		
class FileIterWrapper(object):
	def __init__(self, flo, chunk_size = 1024**2):
		self.flo = flo
		self.chunk_size = chunk_size

	def next(self):
		data = self.flo.read(self.chunk_size)
		if data:
			return data
		else:
			raise StopIteration

	def __iter__(self):
		return self

@login_required	
def browse(request):
    return render_to_response('files/browse.html', {}, context_instance=RequestContext(request))

@login_required
def shares(request):
	sharelist = Share.objects.all()
	for share in sharelist:
		share.filename = os.path.basename(share.path)
	hostname = privateapi.core.gethostname()
	return render_to_response('files/shares.html', { "sharelist": sharelist, "hostname": hostname }, context_instance=RequestContext(request))

@condition(etag_func=None)
def downloadshare(request,shareuuid=''):
	share = Share.objects.get(uuid=shareuuid)
	path = share.path
	mimetype = mimetypes.guess_type(path)
	response = HttpResponse(FileIterWrapper(open(path)), mimetype='%s' % mimetype[0])
	response['Content-Length'] = os.path.getsize(path)
	response['Content-Disposition'] = 'attachment; filename=%s' % os.path.basename(path)
	return response
	
	
@login_required
@csrf_exempt
def addshare(request):
	if request.method == 'POST':
		sharepath = '/media/' + urllib.unquote(request.POST['path'])
		shareuuid = base64.b64encode(str(uuid.uuid4()))
		share = Share(uuid=shareuuid[:10],path=sharepath,public = True)
		form = ShareForm(instance=share)
		
		return render_to_response('files/addshare.html', { "form": form }, context_instance=RequestContext(request))
		
@login_required
def deleteshare(request):
	if request.method == 'POST':
		shareuuid = request.POST['uuid']
		share = Share.objects.get(uuid=shareuuid)
		share.delete()
	return HttpResponseRedirect("/files/shares")
			

@login_required	
def upload(request):
    return render_to_response('files/upload.html', {}, context_instance=RequestContext(request))
	
	
