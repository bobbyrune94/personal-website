"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from personalsite import views

urlpatterns = [
	path('', views.HomeView.as_view(template_name='index.html'), name='home'),
	path('about', views.AboutView.as_view(template_name='about.html'), name='about'),
	path('resume', views.ResumeView.as_view(template_name='resume.html'), name='resume'),
	path('contact', views.ContactView.as_view(template_name='contact.html'), name='contact'),
	path('contact/email', views.send_email, name="send_email"),
	path('projects', views.ProjectsView.as_view(template_name='projects.html'), name='projects'),
	path('projects/SGDGames', views.SGDView.as_view(template_name='projectPages/sgdGames/sgdGames.html'), name='sgd'),
	path('projects/SGDGames/kin', views.KinView.as_view(template_name='projectPages/sgdGames/kin.html'), name='kin'),
	path('projects/SGDGames/duskpatrol', views.DuskPatrolView.as_view(template_name='projectPages/sgdGames/duskpatrol.html'), name='duskpatrol'),
	path('projects/SGDGames/bardstale', views.BardsTaleView.as_view(template_name='projectPages/sgdGames/bardstale.html'), name='bardstale'),
	path('projects/hoohacks', views.HooHacksView.as_view(template_name='projectPages/hackathon/hoohacks.html'), name='hoohacks'),
	path('projects/hoohacks/simplisci', views.SimplisciView.as_view(template_name='projectPages/hackathon/simplisci.html'), name='simplisci'),
	path('projects/hoohacks/faceNormalizer', views.NormalizerView.as_view(template_name='projectPages/hackathon/faceNormalizer.html'), name='normalizer'),
	path('projects/hoohacks/cupanoowords', views.SimplisciView.as_view(template_name='projectPages/hackathon/cupanoowords.html'), name='cupanoowords'),
	path('projects/internships', views.InternView.as_view(template_name='projectPages/internships/internship.html'), name='intern'),
	path('projects/internships/dahlgren', views.DahlgrenView.as_view(template_name='projectPages/internships/dahlgren.html'), name='dahlgren'),
	path('projects/internships/yext', views.YextView.as_view(template_name='projectPages/internships/yext.html'), name='yext'),
	path('projects/classes', views.ClassesView.as_view(template_name='projectPages/classes/classes.html'), name='classes'),
	path('performances', views.PerformancesView.as_view(template_name='performances.html'), name='performances'),
	path('performances/wushu', views.WushuView.as_view(template_name='performancePages/wushu/wushu.html'), name='wushu'),
	path('performances/wushu/uwg', views.UWGView.as_view(template_name='performancePages/wushu/uwg.html'), name='uwg'),
	path('performances/wushu/collegiates', views.CollegiatesView.as_view(template_name='performancePages/wushu/collegiates.html'), name='collegiates'),
	path('performances/wushu/demos', views.DemosView.as_view(template_name='performancePages/wushu/demos.html'), name='demos'),
	path('performances/cheerleading', views.CheerView.as_view(template_name='performancePages/cheerleading/cheerleading.html'), name='cheer'),
	path('performances/cheerleading/cheer2013', views.Cheer2013View.as_view(template_name='performancePages/cheerleading/cheer2013.html'), name='cheer2013'),
	path('performances/cheerleading/cheer2014', views.Cheer2014View.as_view(template_name='performancePages/cheerleading/cheer2014.html'), name='cheer2014'),
	path('performances/cheerleading/cheer2015', views.Cheer2015View.as_view(template_name='performancePages/cheerleading/cheer2015.html'), name='cheer2015'),
    path('admin/', admin.site.urls),
]
