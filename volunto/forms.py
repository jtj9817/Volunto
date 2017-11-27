from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Organization

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta: 
		model = User
		fields = ['username', 'email', 'password']

class ProjectsForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['projectname', 'projdesc', 'projstatus', 'orgname']

class OrganizationForm(forms.ModelForm):
	class Meta:
		model = Organization
		fields = ['orgname', 'orgdesc']