from django import forms
from .models import Track

class new_track(forms.ModelForm):
	class Meta:
		model = Track
		fields= ('name', 'order', 'track_file', 'album', 'artist')