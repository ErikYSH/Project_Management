from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Project, Team
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import TeamForm, ProjectForm
from django.db.models import Count
from django.contrib.admin.widgets import AdminDateWidget

# Create your views here.

#### HOME PAGE FUNCTION
class Home(TemplateView):
    template_name = 'home.html'

#### PROJECT FUNCTION
class Dashboard(TemplateView):
    template_name ='dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        user = self.request.user
        projects = Project.objects.filter(user=user.id)
        print(len(projects))
        project_count = projects.count()
        print(project_count)
        teams = Team.objects.filter(user=user.id)
        team_count = teams.count()
        if name != None: 
            # context['projects_count'] = project_count
            context = {'projects_count':project_count, 'team_count':team_count}
        else: 
            # context['projects_count'] = project_count
            context = {'projects_count':project_count, 'team_count':team_count}
        return context


class Project_Index(TemplateView):
    template_name = 'project_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        user = self.request.user
        projects = Project.objects.filter(user=user.id)
        if name != None: 
            context['projects'] = projects.filter(name__icontains=name) 
        else: 
            context['projects'] = projects
        return context
    

def project_show(request, project_id):
    project = Project.objects.get(id=project_id)
    return render(request, 'project_show.html', {'project':project})

def Project_Create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/projects')
        
    
    form = ProjectForm()
    return render(request, 'project_create.html', {'form':form})

# class Project_Create(CreateView):
#     model = Project
#     fields = ['name', 'description', 'start_date', 'end_date' ,'status','user','team']
#     template_name = "project_create.html"
#     success_url = '/projects'

#     def form_valid(self,form):
#         self.object = form.save(commit=False)
#         self.object.user = self.request.user
#         self.object.save()
#         return HttpResponseRedirect('/projects')
        
class Project_Update(UpdateView):
    model = Project
    fields = ['name', 'description', 'start_date', 'end_date' ,'status','team']
    class_form = ProjectForm
    template_name = 'project_update.html'
    success_url = '/projects'

class Project_Delete(DeleteView):
    model = Project
    template_name = 'project_delete.html'
    success_url = '/projects'

#### PROFILE
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    projects = Project.objects.filter(user=user)
    return render(request, "profile.html", {"username":username, "projects":projects})

#### AUTHENTICATION
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
            messages.success(request, 'The username and/or password is incorrect')
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


#### TEAM FUNCTION
# class Team_Index(TemplateView):
    template_name = 'team_index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        user = self.request.user
        print(user)
        project = Project.objects.filter(user=user.id)
        teams = Team.objects.filter(user=user.id)
        print(teams)
        if name != None: 
            context['teams'] = teams.filter(name__icontains=name) 
        else: 
            context['teams'] = teams
        return context

def Team_Index(request):
    teams = Team.objects.all()
    user = request.user
    teams_login = Team.objects.filter(user=user.id)
    print(teams_login)
    team_count = teams.count()

    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            teams = form.save(commit=False)
            teams.user = request.user
            teams.save()
            return HttpResponseRedirect('/teams')
    else:
        form = TeamForm()
    context = {
        'teams': teams_login,            
        'team_count': team_count,
        'form':form,
    }
    print(context)
    return render(request, 'team_index.html', context)


def team_show(request, team_id):
    team = Team.objects.get(id=team_id)
    return render(request, 'team_show.html', {'team':team})


def Team_Create(request):
    model = Team
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            title = form.cleaned_data['title']
            email = form.cleaned_data['email']
            user = form.cleaned_data['user']
            print(user)
            form.save()
            return HttpResponseRedirect('/teams')

    form = TeamForm()
    return render (request, 'team_create.html', {'form':form})

# class Team_Create(CreateView):
    # model = Team
    # # fields = ['name', 'title','email', 'user']
    # template_name = "team_create.html"
    # success_url = '/teams'

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