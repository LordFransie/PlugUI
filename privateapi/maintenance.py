#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket, os, httplib, urllib
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
	currentmac = privateapi.core.getethermac()
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