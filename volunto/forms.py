from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Organization
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class UserForm(forms.ModelForm):
	username = forms.CharField(max_length=30,min_length=5)
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(widget=forms.EmailInput, required=True)
	class Meta: 
		model = User
		fields = ['username', 'email', 'password']

	def clean_email(self):
		# Get the email
		email = self.cleaned_data.get('email')
		# Check to see if any users already exist with this email as a username.
		try:
			match = User.objects.get(email=email)
		except User.DoesNotExist:
			# Unable to find a user, this is fine
			return email
		# A user was found with this as a username, raise an error.
		raise forms.ValidationError('This email address is already in use.')

class ProjectsForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['projectname', 'projdesc', 'projstatus', 'orgname']

class OrganizationForm(forms.ModelForm):
	class Meta:
		model = Organization
		fields = ['orgname', 'orgdesc']

class ProjectsCreationForm(forms.Form):
	projectname = forms.CharField(max_length=30, min_length=5, required=True)
	projectdesc = forms.CharField(widget=forms.Textarea)
	projstatus = forms.BooleanField(widget=forms.CheckboxInput)
	class Meta:
		model = Project
		fields = '__all__'