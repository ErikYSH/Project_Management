from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Dashboard.as_view(), name='dashboard'),
    path('projects/', views.Project_Index.as_view(), name='project_index'),
    path('projects/<int:project_id>', views.project_show, name='project_show'),
    path('projects/create', views.Project_Create.as_view(), name='project_create'),
    path('projects/<int:pk>/update/', views.Project_Update.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', views.Project_Update.as_view(), name='project_delete'),
]