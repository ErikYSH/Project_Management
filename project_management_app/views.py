from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

# Create your views here.

class Dashboard(TemplateView):
    template_name = 'dashboard.html'
    # def get(self, request):
    #     return HttpResponse("Project Management App")