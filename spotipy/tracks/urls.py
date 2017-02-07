from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^new_track/$', views.track_new, name='track_new'),
	url(r'^track_list/', views.track_list, name='track_list'),
	url(r'^track_edit/(?P<pk>[0-9]+)/$', views.track_edit, name='track_edit'),
	url(r'^track/(?P<pk>[0-9]+)/$', views.track_view, name='track_view'),
	url(r'^eliminar/(?P<pk>[0-9]+)/$', views.track_delete, name='track_delete'),
]