from django import forms
from django.forms import ModelForm
from .models import Meetings

#Create a form
class MeetingForm(ModelForm):
    class Meta:
        model = Meetings
        fields = "__all__"
        labels = {
            'meeting_topic': '',
            'meeting_date': '',
            'meeting_begin_time': '', 
            'meeting_ending_time': '', 
            'meeting_participants': '',
        }
        widgets = {
            'meeting_topic': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Topic'}),
            'meeting_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Date'}),
            'meeting_begin_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Begining Time'}),
            'meeting_ending_time': forms.TimeInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Ending Time'}),
            'meeting_participants': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Meeting Participants'}),
        }
