from django import forms
from .models import Team

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