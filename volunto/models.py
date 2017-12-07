# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Permission
from django.urls import reverse

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
	projectname = models.CharField(max_length=200)
	projdesc = models.CharField(max_length=500)
	projectid = models.AutoField(primary_key=True)
	projstatus = models.BooleanField(default=False)
	orgname = models.ForeignKey(Organization, on_delete=models.CASCADE)
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

