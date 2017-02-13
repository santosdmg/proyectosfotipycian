from django.shortcuts import redirect, render
from .models import Artist
from tracks.models import Track
from django.shortcuts import render, get_object_or_404
from .forms import frmins_artist
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect

@login_required(login_url = '/signin/')
def home(request):
	artists = Artist.objects.all
	return render(request, 'page/index.html', {'artists':artists})

@login_required(login_url = '/signin/')
def det_artist(request, pk):
	artista = get_object_or_404(Artist, pk=pk)
	trackss= Track.objects.filter(artist_id=pk).order_by('order')
	return render(request, 'detartist.html', {'artista':artista,'trackss':trackss})

@login_required(login_url = '/signin/')
@permission_required('artists.add_artist', login_url='/')
def new_artist(request):
	if request.method == "POST":
		form = frmins_artist(request.POST, request.FILES or None)
		if form.is_valid():
			artist= form.save(commit=False)
			artist.save()
			return HttpResponseRedirect('/')

	else:
		form = frmins_artist()
	return render(request, 'new_artist.html', {'form':form})

@login_required(login_url = '/signin/')
@permission_required('artists.edit_artist', login_url='/')
def edit_artist(request, pk):
	artist = get_object_or_404(Artist, pk =pk)
	if request.method == "POST":
		form = frmins_artist(request.POST, request.FILES or None,instance=artist)
		if form.is_valid():
			artist = form.save(commit=False)
			artist.save()
			return HttpResponseRedirect('/')
	else:
		form = frmins_artist(instance = artist)
	return render(request, 'edit_artist.html', {'form':form})
