from django import forms
from .models import Album

class fralbum(forms.ModelForm):
	class Meta:
		model = Album
		fields = ('title', 'cover', 'artist', )
		labels = {
		'title' : ('Titulo '),
		'cover' : ('Portada '),
		'artist' : ('Artista '),
		}
		help_texts = {
		'cover' : ('.jpg, .png')
		}
