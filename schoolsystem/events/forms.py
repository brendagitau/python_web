from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model=Event
        fields='__all__'
        widgets={
        'event_name':forms.TextInput(attrs={'class':'form_control'}),
        'venue':forms.TextInput(attrs={'class':'form_control'}),
        'event_date':forms.DateTimeInput(attrs={'class':'form_control'}),
        'event_description':forms.Textarea(attrs={'class':'form_control','id':'des'}),
        'attendees':forms.EmailInput(attrs={'class':'form_control'}),
       
         }  
     