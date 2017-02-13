from django.db import models

class Artist(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255, blank = True)
	photography = models.ImageField(upload_to = 'artists')
	biography = models.TextField(blank=True)

	def __str__(self):
		return '%s' %(self.first_name+' '+self.last_name)
