from django.shortcuts import render, get_object_or_404
from .models import Album
from tracks.models import Track
from django.http import HttpResponseRedirect
from .forms import fralbum
from django.contrib.auth.decorators import login_required, permission_required

#Nuevo album 
@login_required(login_url='/signin/')
@permission_required('albums.add_album', login_url='/')
def album_new(request):
	if request.method == "POST":
		form = fralbum(request.POST, request.FILES or None)
		if form.is_valid():
			artist= form.save(commit=False)
			artist.save()
			return HttpResponseRedirect('/album_list/')
	else:
		form = fralbum()
	return render(request, 'album_new.html', {'form':form})

#lista de los albumes
@login_required(login_url = '/signin/')
def album_list(request):
	albums= Album.objects.all
	return render(request, 'albums_list.html', {'albums':albums})

@login_required(login_url = '/signin/')
@permission_required('artists.edit_album', login_url='/')
def album_edit(request, pk):
	album = get_object_or_404(Album, pk =pk)
	if request.method == "POST":
		form = fralbum(request.POST, instance=album)
		if form.is_valid():
			album = form.save(commit=False)
			album.save()
			return HttpResponseRedirect('/album_list/')
	else:
		form = fralbum(instance = album)
	return render(request, 'album_edit.html', {'form':form})


#detalle de cada album
@login_required(login_url = '/signin/')
def det_album(request, pk):
	album = get_object_or_404(Album, pk=pk)
	tracks = Track.objects.filter(album_id=pk).order_by('order')
	tam = len(tracks)
	return render(request, 'det_album.html', {'album':album, 'tracks':tracks, 'tam':tam})

