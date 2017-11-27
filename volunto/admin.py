# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Organization, Project, School, Volunteer, Position

# Register your models here.
admin.site.register(Project),
admin.site.register(School),
admin.site.register(Volunteer),
admin.site.register(Organization),
admin.site.register(Position)