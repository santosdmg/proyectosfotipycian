import json
from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Track
from .forms import new_track
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required

@login_required(login_url = '/signin/')
def track_view(request, pk):
	#try:
	#	track = Track.objects.get(name=name)
	#except Track.DoesNotExist:
	#	raise Http404

	#track = get_object_or_404(Track, name=name)
	
	#---para retornar en formato Json
	#data = {
	#	'name' : track.name,
	#	'order' : track.order,
	#	'album' : track.album.title,
	#	'artist' : {
	#		'name' : track.artist.first_name,
	#		'bio' : track.artist.biography,
	#	}
	#}
	#json_data = json.dumps(data)
	#return HttpResponse(json_data, content_type='application/json')
	#--Json
	#return render(request, 'track.html', {'track':track})

	track = get_object_or_404(Track, pk=pk)
	return render(request, 'track.html', {'track':track})



#Lista de track
@login_required(login_url = '/signin/')
def track_list(request):
	tracks = Track.objects.all().order_by('order')

	return render(request, 'track_list.html', {'tracks':tracks})


#Nuevo track
@login_required(login_url = '/signin/')
@permission_required('tracks.add_track', login_url='/')
def track_new(request):
	if request.method == "POST":
		form = new_track(request.POST, request.FILES or None)
		if form.is_valid():
			track = form.save(commit=False)
			track.save()
			return HttpResponseRedirect('/track_list/')
	else:
		form= new_track()
	return render(request, 'track_new.html', {'form':form})

#Editar track
@login_required(login_url = '/signin/')
@permission_required('tracks.edit_track', login_url='/')
def track_edit(request, pk):
	track = get_object_or_404(Track, pk=pk)
	if request.method == "POST":
		form = new_track(request.POST, instance=track)
		if form.is_valid():
			track = form.save(commit=False)
			track.save()
			return HttpResponseRedirect('/track_list')
	else:
		form = new_track(instance = track)
	return render(request, 'track_edit.html', {'form':form})


#Eliminar track
@login_required(login_url = '/signin/')
@permission_required('tracks.delete_track', login_url='/')
def track_delete(request, pk=None):
	track = get_object_or_404(Track, pk=pk)
	track.delete()
	return HttpResponseRedirect('/track_list')