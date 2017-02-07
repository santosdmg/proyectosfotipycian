from django.conf.urls import include, url
from . import views

urlpatterns = [
	url(r'^signup/', views.signup, name='signup'),
    url(r'^signin/', views.signin, name='signin'),
    url(r'^signout/', views.signout, name='signout'),
]