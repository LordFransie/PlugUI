"""
Copyright (c) 2009, Steve Oliver (steve@xercestech.com)
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the 
      documentation and/or other materials provided with the distribution.
    * Neither the name of the <organization> nor the
      names of its contributors may be used to endorse or promote products
      derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY STEVE OLIVER ''AS IS'' AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL STEVE OLIVER BE LIABLE FOR ANY
DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;                    
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND 
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."""

from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from django import forms
import os
import privateapi.core
import privateapi.minidlna
import privateapi.samba

class MinidlnaForm(forms.Form):
	BOOLEAN_CHOICES = (
		('no', 'No'),
		('yes', 'Yes'),
	)	
	strict_dlna = forms.ChoiceField(choices=BOOLEAN_CHOICES)
	enable_tivo = forms.ChoiceField(choices=BOOLEAN_CHOICES)
	inotify = forms.ChoiceField(choices=BOOLEAN_CHOICES)
	#album_art_names = forms.CharField(max_length=300)
	media_dir = forms.CharField()
	port = forms.CharField()


@login_required
def index(request): 
    installed_apps = os.listdir("/etc/installed_apps/")
    return render_to_response('apps/index.html', { "installed_apps": installed_apps },context_instance=RequestContext(request))

@login_required
def minidlna(request): 
	installed_apps = os.listdir("/etc/installed_apps/")
	if request.method == 'POST':
		form = MinidlnaForm(request.POST)
		if form.is_valid():
			dict = {}
			dict['strict_dlna'] = form.cleaned_data['strict_dlna']
			dict['enable_tivo'] = form.cleaned_data['enable_tivo']
			dict['media_dir'] = form.cleaned_data['media_dir']
			dict['inotify'] = form.cleaned_data['inotify']
			dict['port'] = form.cleaned_data['port']
			privateapi.minidlna.set_config(dict)
			#return HttpResponseRedirect("/apps/minidlna")
			return render_to_response('apps/minidlna.html', { "installed_apps": installed_apps, "form": form },context_instance=RequestContext(request))
		else:
			return render_to_response('apps/minidlna.html', { "installed_apps": installed_apps, "form": form },context_instance=RequestContext(request))
	else:
		config_dict = privateapi.minidlna.get_config()
		form = MinidlnaForm(initial=config_dict)
		return render_to_response('apps/minidlna.html', { "installed_apps": installed_apps, "form": form },context_instance=RequestContext(request))

@login_required
def samba(request): 
    installed_apps = os.listdir("/etc/installed_apps/")
    return render_to_response('apps/samba.html', { "installed_apps": installed_apps },context_instance=RequestContext(request))


