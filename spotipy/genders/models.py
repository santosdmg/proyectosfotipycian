from django.db import models
from albums.models import Album
from artists.models import Artist

class Gender(models.Model):
	name = models.CharField(max_length=255)
	album = models.ManyToManyField(Album)
	artist = models.ManyToManyField(Artist)


	def __str__(self):
		return self.name


