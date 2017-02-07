from django.conf.urls import include, url
from . import views

urlpatterns = [
url(r'^album_new/$', views.album_new, name='album_new'),
	url(r'^det_album/(?P<pk>[0-9]+)/$', views.det_album, name='det_album'),
	url(r'^album_list/$', views.album_list, name='album_list'),
	url(r'^album_edit/(?P<pk>[0-9]+)/$', views.album_edit, name='album_edit'),
	
]