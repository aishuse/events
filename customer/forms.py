from django import forms

from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'image', 'venue', 'date', 'start_time', 'end_time']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            "date": forms.DateInput(attrs={"type": "date"}),
            "start_time" : forms.TimeInput(attrs={'type': 'time'}),
            "end_time": forms.TimeInput(attrs={'type': 'time'}),
        }