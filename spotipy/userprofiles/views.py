from django.shortcuts import render
from django.contrib.auth import login, logout
from .forms import UserCreationEmailForm, EmailAuthenticationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

def signup(request):
	form = UserCreationEmailForm(request.POST or None)

	if form.is_valid():
		form.save()

	return render(request, 'tuser/signup.html', {'form':form})


def signin(request):
	form = EmailAuthenticationForm(request.POST or None)

	if form.is_valid():
		login(request, form.get_user())
		return HttpResponseRedirect('/')

	return render(request, 'tuser/signin.html', {'form':form})

@login_required(login_url = '/signin/')
def signout( request):
	logout(request)
	return HttpResponseRedirect('/')
