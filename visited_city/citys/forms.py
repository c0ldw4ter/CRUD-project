from django import forms
from .models import City

class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['city', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}) 
        }