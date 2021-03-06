#!/usr/bin/env python 
# coding: utf8
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
import shlex, subprocess, re, socket, os, httplib, urllib, base64
import feedparser
from home.models import PlugappsNewsEntry
from system.models import MaintenanceStats
import privateapi.pacman
import privateapi.core


def update_plugapps_news():
	PlugappsNewsEntry.objects.all().delete()
	plugappsfeed = feedparser.parse("http://dev2.plugapps.com/category/news/feed/")
	feed_items = plugappsfeed['entries']
	for story in feed_items:
		item = PlugappsNewsEntry()
		item.title = story['title']
		item.description = story['description']
		#item.date = story['date']
		item.link = story['link']
		item.save()

def update_plug_location():
	currentmac = base64.b64encode(str(privateapi.core.getethermac()))[:10]
	currentip = privateapi.core.getcurrentip()
	params = urllib.urlencode( { 'plugid': currentmac, 'localip': currentip } )
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn = httplib.HTTPConnection("plugfinder.appspot.com:80")
	conn.request("POST", "/", params, headers)
	conn.close()

def run_maintenance():
	update_plugapps_news()
	update_plug_location()
	if privateapi.pacman.check():
		privateapi.pacman.list_upgrades()
	maintenancestats = MaintenanceStats()
	maintenancestats.save()