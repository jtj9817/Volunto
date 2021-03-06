from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from . import views
from volunto.views import ProjectListView , OrganizationListView, ProjectUpdate, ProjectDelete
from .views import ProfileDetail, ProfileUpdate
from django.contrib.auth import \
    views as auth_views
from django.contrib.auth.forms import \
    AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.views.generic import (RedirectView, TemplateView)


app_name = 'volunto'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^projects/$', views.ProjectListView.as_view(), name='projects'),
    url(r'^organizations/$', views.OrganizationListView.as_view(), name='organizations'),
    url(r'^projects/create/$', views.ProjectCreate.as_view(), name='project_create'),
    url(r'^create_application/$', views.ApplicationCreate.as_view(), name='create_application'),
    url(r'^create_application/application_sent/$', views.application_sent, name='application_sent'),
    url(r'^project/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^project/update/(?P<pk>\d+)$', views.ProjectUpdate.as_view(), name='project_update'),
    url(r'^project/delete/(?P<pk>\d+)$', views.ProjectDelete.as_view(), name='project_delete'),
    url(r'^organization/(?P<pk>\d+)$', views.OrganizationDetailView.as_view(), name='organization-detail'),
    url(r'^accounts/update/(?P<pk>[\-\w]+)/$', views.edit_profile, name='account_update'),
    url(r'^profile/$',views.ProfileDetail.as_view(), name="profile"),
    url(r'^profile/edit/$', views.ProfileUpdate.as_view(), name="profile_update")
]