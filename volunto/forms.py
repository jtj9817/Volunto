from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Project, Organization
from django.core.validators import validate_email

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	class Meta: 
		model = User
		fields = ['username', 'email', 'password']

	def clean_email(self):
		# Get the email
		email = self.cleaned_data.get('email')
		try:
			validate_email(email)
		except validate_email.ValidationError:
    			print('Invalid email address')
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
