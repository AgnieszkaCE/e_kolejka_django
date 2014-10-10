from django import forms
from cpracownik.models import Info

class InfoForm(forms.ModelForm):
    
    class Meta:
        model = Info
        fields = ('temat','tresc', 'data', 'p')
        
        