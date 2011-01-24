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
from django.template import RequestContext
from django import forms
import privateapi.core
import privateapi.pacman
from system.models import MaintenanceStats
from django.contrib.auth.decorators import login_required

class AdvancedForm(forms.Form):
	TRIGGER_CHOICES = (
		('none', 'No Trigger'),
		('nand-disk', 'NAND Activity'),
		('mmc0', 'SD Activity'),
		('timer', 'Timer'),
		('heartbeat', 'Heartbeat'),
		('default-on', 'Default on'),
	)
	green_trigger = forms.ChoiceField(choices=TRIGGER_CHOICES)
	orange_trigger = forms.ChoiceField(choices=TRIGGER_CHOICES)
	AUTOMOUNT_CHOICES = (
		('false', 'No'),
		('true', 'Yes'),
	)	
	sdautomount = forms.ChoiceField(choices=AUTOMOUNT_CHOICES)
	usbautomount = forms.ChoiceField(choices=AUTOMOUNT_CHOICES)

@login_required
def index(request):
	currentip = privateapi.core.getcurrentip()
	currentuptime = privateapi.core.getuptime() 
	load = privateapi.core.getloadavg()
	memfree = privateapi.core.getmemory_free() 
	memtotal = privateapi.core.getmemory_total()
	memused = str(int(memtotal) - int(memfree))
	percentused = str(100 - int(privateapi.core.getmemory_percent()))
	currentip = privateapi.core.getcurrentip()
	kernelversion = privateapi.core.getkernelversion()
	devicename = privateapi.core.getdevicename()
	processor = privateapi.core.getprocessor()
	architecture = privateapi.core.getarchitecture()
	stats = {"currentip": currentip, "currentuptime": currentuptime, "load": load, "memused": memused, "memfree": memfree, "memtotal": memtotal, "percentused": percentused, "currentip": currentip, "kernelversion": kernelversion, "devicename": devicename, "processor": processor, "architecture": architecture } 
	return render_to_response('system/index.html', stats, context_instance=RequestContext(request))

@login_required
def storage(request):
	mounted_device_list = privateapi.core.mounted_devices()
	mounted_device_details = privateapi.core.mount_details()
	number_of_mounts = len(mounted_device_list)
	stats = { "mounted_device_list": mounted_device_list, "mounted_device_details": mounted_device_details, "number_of_mounts": number_of_mounts }
	return render_to_response('system/storage.html', stats, context_instance=RequestContext(request))

@login_required   
def networking(request):
	currentip = privateapi.core.getcurrentip()
	stats = { "currentip": currentip }
	return render_to_response('system/networking.html', stats, context_instance=RequestContext(request))
    
@login_required  
def software(request):
	installed_packages = privateapi.pacman.list_installed()
	return render_to_response('system/software.html', { "installed_packages": installed_packages }, context_instance=RequestContext(request))

@login_required
def reboot(request):
	return render_to_response('system/reboot.html', {}, context_instance=RequestContext(request))


@login_required
def advanced(request):
	try:
		maintenance_stats = MaintenanceStats.objects.get(id=1)
		last_maintenance = maintenance_stats.last_maintenance
	except:
		last_maintenance = 'some point in the near future'
	if request.method == 'POST':
		form = AdvancedForm(request.POST)
		if form.is_valid():
			privateapi.core.set_led('green',form.cleaned_data['green_trigger'])
			privateapi.core.set_led('orange',form.cleaned_data['orange_trigger'])
			if 'true' in form.cleaned_data['usbautomount']:
				usbsetting = True
			else:
				usbsetting = False
			if 'true' in form.cleaned_data['sdautomount']:
				sdsetting = True
			else:
				sdsetting = False				
				
			privateapi.core.set_automount(usb=usbsetting,sd=sdsetting)
	else:
		led_dict = privateapi.core.get_leds()
		automount_dict = privateapi.core.get_automount()
		if automount_dict['usbautomount'] == True:
			automount_dict['usbautomount'] = 'true'
		elif automount_dict['usbautomount'] == False:
			automount_dict['usbautomount'] = 'false'
		if automount_dict['sdautomount'] == True:
			automount_dict['sdautomount'] = 'true'
		elif automount_dict['sdautomount'] == False:
			automount_dict['sdautomount'] = 'false'			
			
		form_dict = dict(led_dict.items() + automount_dict.items())
		form = AdvancedForm(initial=form_dict)
		
	return render_to_response('system/advanced.html', { "form": form, "last_maintenance": last_maintenance }, context_instance=RequestContext(request))
	