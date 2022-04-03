from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Project, Team
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class Home(TemplateView):
    template_name = 'home.html'

# PROJECT FUNCTION
class Dashboard(TemplateView):
    template_name ='dashboard.html'

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

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/projects')
        
class Project_Update(UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date' ,'status',]
    template_name = 'project_update.html'
    success_url = '/projects'

class Project_Delete(DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = '/projects'

# PROFILE
def profile(request, username):
    user = User.objects.get(username=username)
    projects = Project.objects.filter(user=user)
    return render(request, "profile.html", {"username":username, "projects":projects})

# AUTHENTICATION
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']  
            p = form.cleaned_data['password'] 
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/dashboard')
                else:
                    print('The account has been disabled')
                    return HttpResponseRedirect('/login')
        else:
            print('The username and/or password is incorrect')
            return HttpResponseRedirect('/login')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('HEY', user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else:
            return render(request, 'signup.html', {'form': form})

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


# TEAM FUNCTION
class Team_Index(TemplateView):
    template_name = 'team_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        if name != None: 
            context['teams'] = Team.objects.filter(name_icontains=name) 
        else: 
            context['teams'] = Team.objects.all
        return context

def team_show(request, team_id):
    team = Team.objects.get(id=team_id)
    return render(request, 'team_show.html', {'team':team})

class Team_Create(CreateView):
    model = Team
    fields = "__all__"
    template_name = "team_create.html"
    success_url = '/teams'

    # def form_valid(self,form):
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return HttpResponseRedirect('/teams')
        

class Team_Update(UpdateView):
    model = Team
    fields = "__all__"
    template_name = 'team_update.html'
    success_url = '/teams'

class Team_Delete(DeleteView):
    model = Team
    template_name = 'team_delete.html'
    success_url = '/teams'