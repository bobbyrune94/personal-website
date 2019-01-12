from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import generic
from django.core.mail import BadHeaderError, send_mail
from django.shortcuts import redirect

# Create your views here.

class HomeView(TemplateView):
	template_name = "base.html"

class AboutView(TemplateView):
	template_name = "about.html"

class ResumeView(TemplateView):
	template_name = "resume.html"

class ContactView(TemplateView):
	template_name = "contact.html"

class ProjectsView(TemplateView):
	template_name = "project.html"

class SGDView(TemplateView):
	template_name = "projectPages/sgdgames/sgdGames.html"

class KinView(TemplateView):
	template_name = "projectPages/sgdgames/kin.html"

class DuskPatrolView(TemplateView):
	template_name = "projectPages/sgdgames/duskpatrol.html"

class BardsTaleView(TemplateView):
	template_name = "projectPages/sgdgames/bardstale.html"

class HooHacksView(TemplateView):
	template_name = "projectPages/hackathon/hoohacks.html"

class SimplisciView(TemplateView):
	template_name = "projectPages/hackathon/simplisci.html"

class NormalizerView(TemplateView):
	template_name = "projectPages/hackathon/faceNormalizer.html"

class InternView(TemplateView):
	template_name = "projectPages/internships/internship.html"

class DahlgrenView(TemplateView):
	template_name = "projectPages/internships/dahlgren.html"

class YextView(TemplateView):
	template_name = "projectPages/internships/yext.html"

class ClassesView(TemplateView):
	template_name = "projectPages/classes/classes.html"

class PerformancesView(TemplateView):
	template_name = "performances.html"

class WushuView(TemplateView):
	template_name = "performancePages/wushu/wushu.html"

class UWGView(TemplateView):
	template_name = "performancePages/wushu/uwg.html"

class CollegiatesView(TemplateView):
	template_name = "performancePages/wushu/collegiates.html"

class DemosView(TemplateView):
	template_name = "performancePages/wushu/demos.html"

class CheerView(TemplateView):
	template_name = "performancePages/cheerleading/cheerleading.html"

class Cheer2013View(TemplateView):
	template_name = "performancePages/cheerleading/cheer2013.html"

class Cheer2014View(TemplateView):
	template_name = "performancePages/cheerleading/cheer2014.html"

class Cheer2015View(TemplateView):
	template_name = "performancePages/cheerleading/cheer2015.html"

def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        from_email = request.POST.get('email')
        message = request.POST.get('message')
        to_email = 'bobbyrune94@gmail.com'
        subject = "[Website] Message from " + name + " at " + from_email
        
        try:
            send_mail(subject, message, from_email, [to_email])
            return redirect('/contact?sent=true')
        except BadHeaderError:
            return redirect('/contact?sent=false')
    else:
        return redirect('/contact?sent=false')