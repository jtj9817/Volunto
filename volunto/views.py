# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.views import generic
from .models import Project, Organization 
from django.contrib.auth.decorators import login_required


# Create your views here.
# attached @login_required later once log_in system has been implemented
def index(request):
	return render(request, 'volunto/index.html')

def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return render(request, 'volunto/index.html')
			else:
				return render(request, 'volunto/login.html', {'error_message': 'Account is disabled.'})
		else:
			return render(request, 'volunto/login.html', {'error_message': 'Invalid login'})
	return render(request, 'volunto/login.html')		
#User submits the form filled with data in a POST request
def register(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user= form.save(commit=False)
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			user = authenticate(username=username, password=password)
			login(request, user)
			return render(request,'volunto/index.html')
	else:
		form = UserForm()
	return render(request, 'volunto/registration_form.html', {'form': form})
def logout_user(request):
	return render(request, 'volunto/logout.html')		
#Views for Projects 
class ProjectListView(generic.ListView):
	model = Project
	context_object_name = 'projects_list'
	template_name = 'volunto/project_list.html'

	def get_queryset(self):
		return Project.objects.all()

class ProjectDetailView(generic.DetailView):
	model = Project

#Views for Organizations
class OrganizationListView(generic.ListView):
	model = Organization 
	context_object_name = 'organizations_list'
	template_name = 'volunto/organization_list.html'

	def get_queryset(self):
		return Organization.objects.all()

class OrganizationDetailView(generic.DetailView):
	model = Organization