from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^det_artist/(?P<pk>[0-9]+)/$', views.det_artist, name='det_artist'),
	url(r'^new_artist/$', views.new_artist, name='new_artist'),
	url(r'^edit_artist/(?P<pk>[0-9]+)/$', views.edit_artist, name='edit_artist'),
]