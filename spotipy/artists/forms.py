from django import forms
from .models import Artist

class frmins_artist(forms.ModelForm):
	class Meta:
		model = Artist
		fields = ('first_name', 'last_name', 'biography', 'photography')
		labels = {
		'first_name' : ('Nombre'),
		'last_name' : ('Apellido'),
		'biography' : ('Biografía'),
		'photography' : ('Fotografía'),

		}
		help_texts = {
		'photography' : ('.jpg, .png')
		}
