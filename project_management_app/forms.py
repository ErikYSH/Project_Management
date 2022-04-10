from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from .models import Team, Project

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ("name", "title", "email", "user")
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Title'}),
            'user': forms.Select(attrs={'class':'form-control','value':'user'}),
        }


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'description', 'start_date', 'end_date' ,'status','user','team')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'description': forms.Textarea(attrs={'class':'form-control','value':'description'}),
            'start_date': forms.TextInput(attrs={'class':'form-control','placeholder':'Start Date'}),
            'end_date': forms.TextInput(attrs={'class':'form-control','placeholder':'End Date'}),
            'status': forms.Select(attrs={'class':'form-control','value':'status'}),
            'user': forms.Select(attrs={'class':'form-control','value':'user'}),
            'team': forms.SelectMultiple(attrs={'class':'form-control'}),
        }