from django import forms
from django.forms.widgets import Widget
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields ="__all__"
        Widget = {
        

        }  


