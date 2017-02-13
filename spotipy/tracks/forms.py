from django import forms
from .models import Track

class new_track(forms.ModelForm):
	class Meta:
		model = Track
		fields= ('name', 'order', 'track_file', 'album', 'artist')
		labels = {
		'name' : ('Nombre de la pista'),
		'order' : ('Orden'),
		'track_file' : ('Pista'),
		'album' : ('Album'),
		'artist' : ('Artista'),
		}
		help_texts = {
		'track_file' : ('.mp3')
		}
