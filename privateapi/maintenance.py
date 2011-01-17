#!/usr/bin/env python 
# coding: utf8

import shlex, subprocess, re, socket, os
import feedparser
from home.models import PlugappsNewsEntry
from system.models import MaintenanceStats
import privateapi.pacman



def update_plugapps_news():
	PlugappsNewsEntry.objects.all().delete()
	plugappsfeed = feedparser.parse("http://dev.plugapps.com/category/news/feed/")
	feed_items = plugappsfeed['entries']
	for story in feed_items:
		item = PlugappsNewsEntry()
		item.title = story['title']
		item.description = story['description']
		#item.date = story['date']
		item.link = story['link']
		item.save()

def run_maintenance():
	update_plugapps_news()
	if privateapi.pacman.check():
		privateapi.pacman.list_upgrades()
	maintenancestats = MaintenanceStats()
	maintenancestats.save()