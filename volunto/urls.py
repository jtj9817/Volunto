from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from . import views
from volunto.views import ProjectListView 

app_name = 'volunto'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^projects/$', views.ProjectListView.as_view(), name='projects'),
    url(r'^organizations/$', views.OrganizationListView.as_view(), name='organizations'),
    url(r'^create_project/$', views.create_project, name='create_project'),
    url(r'^projects/create/$', views.ProjectCreate.as_view(), name='project_create'),
    url(r'^project/(?P<pk>\d+)$', views.ProjectDetailView.as_view(), name='project-detail'),
    url(r'^organization/(?P<pk>\d+)$', views.OrganizationDetailView.as_view(), name='organization-detail'),    
    #url(r'^(?P<pk>[-\w]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
]