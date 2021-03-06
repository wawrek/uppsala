from django.shortcuts import render_to_response, get_object_or_404
from uppsala.meet.models import Meet
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from uppsala.meet.forms import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def index(request):
	return render_to_response('users/index.html',{})

def login_user(request):
	username_login = request.POST['username']
	password_login = request.POST['password']
	user = authenticate(username=username_login, password=password_login)
	if user is not None:
		login(request, user)
		return render_to_response('users/status.html',{'status':'log_success'} )
	else:
		return render_to_response('users/status.html',{'status':'log_fail'})

def register(request):
	user_new = request.POST['username']
	password_new = request.POST['password']
	email_new = request.POST['email']
	user = User.objects.create_user(user_new,email_new,password_new)
	return render_to_response('users/status.html',{'status':'reg_success' })
