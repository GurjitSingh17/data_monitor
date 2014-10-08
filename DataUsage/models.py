from django.db import models

# Create your models here.

class Day(models.Model):
	download = models.DecimalField(max_digits=20,decimal_places=2)
	upload = models.DecimalField(max_digits=20,decimal_places=2)
	total = models.DecimalField(max_digits=20,decimal_places=2)
	date = models.DateField()

	def __unicode__(self):
		return "day: {0} | dl: {1} | ul: {2} | total: {3}".format(self.date,self.download,self.upload,self.total)
	def __str__(self):
		return "day: {0} | dl: {1} | ul: {2} | total: {3}".format(self.date,self.download,self.upload,self.total)
