from django.db import models

class SystemStats(models.Model):

	updatecount = models.CharField(max_length=256,editable=True)
	updatesavailable = models.BooleanField(default=False,editable=True)

	def __unicode__(self):
		return u'System stats'
		
	def save(self):
		self.id=1
		super(SystemStats, self).save()

	def delete(self):
		pass
		
class MaintenanceStats(models.Model):
	last_maintenance = models.DateTimeField(auto_now=True, auto_now_add=True)
	def __unicode__(self):
		return u'Maintenance stats'
		
	def save(self):
		self.id = 1
		super(MaintenanceStats, self).save()

	def delete(self):
		pass