from django.db import models
from django.contrib.auth.models import User
from tracks.models import Track

class Playlist(models.Model):
	name = models.CharField(max_length=255)
	track = models.ManyToManyField(Track, blank=True)
	user = models.ManyToManyField(User, blank=True)

	def __str__(self):
		return self.name