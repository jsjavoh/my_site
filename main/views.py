from django.shortcuts import render, redirect
from django.views import View
from .models import Project
from .forms import ContactForm



class HomePage(View):
    def get(self, request):
        return render(request, 'home.html')

class AboutPage(View):
    def get(self, request):
        return render(request, 'about.html')

class SkillsPage(View):
    def get(self,request):
        return render(request, 'skills.html')

class ProjectsPage(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, 'portfolio.html', {'projects':projects})

class ConntactPage(View):

    def get(self, request):
        form = ContactForm()
        return  render(request,'contact.html',{'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'contact.html', {'form': form})

