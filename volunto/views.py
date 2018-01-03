# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserForm, ProjectsForm
from django.views import generic
from .models import Project, Organization, Application
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

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
			return render(request,'volunto/registersuccess.html')
	else:
		form = UserForm()
	return render(request, 'volunto/registration_form.html', {'form': form})
def logout_user(request):
	return render(request, 'volunto/logout.html')		
#Views for Projects 
class ProjectListView(LoginRequiredMixin,generic.ListView):
	model = Project
	context_object_name = 'projects_list'
	queryset = Project.objects.all()
	template_name = 'volunto/project_list.html'

	def get_queryset(self):
		return Project.objects.all()
	def get_context_data(self, **kwargs):
		context = super(ProjectListView, self).get_context_data(**kwargs)
		context['Temp data'] = 'Temp data for projects'
		return context

class ProjectDetailView(LoginRequiredMixin,generic.DetailView):
	model = Project
	template_name = "volunto/project_detail.html"

class ProjectCreate(LoginRequiredMixin,CreateView):
	model = Project
	fields = '__all__'


#Views for Organizations

class OrganizationListView(LoginRequiredMixin,generic.ListView):
	model = Organization 
	queryset = Organization.objects.all()
	context_object_name = 'organizations_list'
	template_name = 'volunto/organization_list.html'

	def get_queryset(self):
		return Organization.objects.all()
	def get_context_data(self, **kwargs):
		context = super(OrganizationListView, self).get_context_data(**kwargs)
		context['Temp data'] = 'Temp data for org'
		return context

class OrganizationDetailView(generic.DetailView):
	model = Organization
	template_name = 'volunto/organization_detail.html'

# Views for Application
class ApplicationCreate(LoginRequiredMixin,CreateView):
	model = Application
	fields = '__all__'
	success_url = 'application_sent/'

def application_sent(request):
	return render(request, 'volunto/application_sent.html')


## These views are to be used in near future
def join_project(request):
	if request.method == 'POST':
		form = ProjectsForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			projectname = form.cleaned_data.get('projectname')
			projdesc = form.cleaned_data.get('password')
			projstatus = form.cleaned_data.get('projstatus')
			project.save()
			return render(request,'volunto/project_success.html')
	else:
		form = ProjectsForm()
	return render(request, 'volunto/project_join.html')


##Unused project creation
def create_project(request):
	if request.method == 'POST':
		form = ProjectsForm(request.POST)
		if form.is_valid():
			project = form.save(commit=False)
			projectname = form.cleaned_data.get('projectname')
			projdesc = form.cleaned_data.get('password')
			projstatus = form.cleaned_data.get('projstatus')
			project.save()
			return render(request,'volunto/project_success.html')
	else:
		form = ProjectsForm()
	return render(request, 'volunto/project_create.html')#, {'form': form})