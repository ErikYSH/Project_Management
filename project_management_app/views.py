from pipes import Template
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Dashboard(TemplateView):
    template_name = 'dashboard.html'

class Project_Index(TemplateView):
    template_name = 'project_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None: 
            context['projects'] = Project.objects.filter(name_icontains=name) 
        else: 
            context['projects'] = Project.objects.all
        return context

def project_show(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_show.html', {'project':project})

class Project_Create(CreateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date' ,'status','user']
    template_name = "project_create.html"
    success_url = '/projects'

class Project_Update(UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date' ,'status',]
    template_name = 'project_update.html'
    success_url = '/projects'

class Project_Delete(DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = '/projects'