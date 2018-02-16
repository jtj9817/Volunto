# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Permission
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

# Create your models here.

class Organization(models.Model):
	orgname = models.CharField(max_length=200)
	orgdesc = models.TextField(max_length=200)
	orgid = models.AutoField(primary_key=True)
	orgusername = models.CharField(max_length=200)
	orgpw = models.CharField(max_length=30, default="")
	ORG_STATUS = (
		(1, 'Active'),
		(2, 'Inactive'),
		(3, 'In-review')
		)
	orgstat = models.PositiveIntegerField(choices=ORG_STATUS, default=3)
	def __str__(self):
		return self.orgname
	def get_absolute_url(self):
		#Returns a URL for accessing an Organization object instance
		return reverse('volunto:organization-detail', args=(self.orgid,))

class Project(models.Model):
	projectname = models.CharField("Project Name",max_length=200)
	projdesc = models.CharField("Project Description",max_length=500)
	projectid = models.AutoField(primary_key=True)
	projstatus = models.BooleanField("Project Status", default=False)
	orgname = models.ForeignKey(Organization, on_delete=models.CASCADE, verbose_name="Project Sponsor")
	def __str__(self):
		return self.projectname
	def get_absolute_url(self):
		#Returns a URL for accessing a Project object instance
		return reverse('volunto:project-detail', args=(self.projectid,))

class School(models.Model):
	schoolname = models.CharField(max_length=200)
	schooladdress = models.CharField(max_length=200)
	schoolid = models.AutoField(primary_key=True)
	def __str__(self):
		return self.schoolname

class Volunteer(models.Model):
	volunteerid = models.AutoField(primary_key=True)
	school = models.ForeignKey(School,on_delete=models.CASCADE, default=1)
	birth_date = models.DateField(null=True, blank=True)

class Position(models.Model):
	postitle = models.CharField(max_length=50)
	posdesc = models.TextField(max_length=200)
	POS_LEVELS = (
		(1, 'Basic'),
		(2, 'Immediate'),
		(3, 'Advanced')
		)
	level = models.PositiveIntegerField(choices=POS_LEVELS, default=1)
	posid = models.AutoField(primary_key=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, default=1)
	def __str__(self):
		return self.postitle

class Application(models.Model):
	applicationid = models.AutoField(primary_key=True)
	project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name="Project Name")
	applicant_firstname = models.CharField("First Name",max_length=30)
	applicant_lastname = models.CharField("Last Name",max_length=30)

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	slug = models.SlugField(max_length=30,unique=True, null=True, default=None)
	bio = models.TextField(max_length=500, blank=True)
	location = models.CharField(max_length=30, blank=True)
	phone = models.CharField(max_length=10, blank=True)
	experience_level_choices = (
		(1, 'No Experience'),
		(2, 'Some Experience'),
		(3, 'Experienced with certification')
		)
	experience_level = models.PositiveIntegerField(choices=experience_level_choices, default=1)
	experience_area_choices =(
		(1, 'Technology'),
		(2, 'Hospitality'),
		(3, 'Education'),
		(4, 'Miscellaneous')
		)
	experience_area = models.PositiveIntegerField(choices=experience_area_choices, default=4)
	education_level_choices = (
		(1, 'Secondary'),
		(2, 'Post Secondary')
		)
	education_level = models.PositiveIntegerField(choices=education_level_choices, default=1)

	#Verbose name for Django Admin interface of Profile
	def __str__(self):
		return self.user.username

	#Use to redirect to Profile Update page
	def get_update_url(self):
		return reverse('dj-auth:profile_update')

	def get_absolute_url(self):
		return reverse('dj-auth:profile')
	#Methods to create and update Profile once a User was created
	def create_profile(sender, **kwargs):
		user=kwargs["instance"]
		if kwargs["created"]:
			user_profile = Profile(user=user)
			user_profile.save()
	post_save.connect(create_profile, sender=User)