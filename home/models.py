from django.db import models

class PlugappsNewsEntry(models.Model):
	title = models.CharField(max_length=256)
	description = models.TextField()
	#date = models.DateField()
	link = models.CharField(max_length=256)