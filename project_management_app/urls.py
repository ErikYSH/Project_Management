from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('dashboard/', views.Dashboard.as_view(), name="dashboard"),
    path('projects/', views.Project_Index.as_view(), name='project_index'),
    path('projects/<int:project_id>', views.project_show, name='project_show'),
    path('projects/create', views.Project_Create.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', views.Project_Update.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.Project_Delete.as_view(), name='project_delete'),

    path('user/<username>', views.profile, name="profile"),

    path('/login', views.login_view, name="login"),
    path('/logout', views.logout_view, name="logout"),
    path('/signup', views.signup_view, name="signup"),

    path('teams/', views.Team_Index.as_view(), name="team_index"),
    path('teams/<int:team_id>', views.team_show, name="team_show"),
    path('teams/create', views.Team_Create.as_view(), name="team_create"),
    path('teams/<int:pk>/update/', views.Team_Update.as_view(), name="team_update"),
    path('teams/<int:pk>/delete/', views.Team_Delete.as_view(), name="team_delete"),
]