from django import forms
from django.forms import DateInput
from .models import JournalLog

"""
Form for creating and updating a journal. 
The user can specify the date when the journal was created, and add content to 
their journal. 
"""


class JournalForm(forms.ModelForm):
    class Meta:
        model = JournalLog
        fields = ['created_on', 'content']
        ordering = ['-created_on']
        widgets = {
            'created_on': DateInput(attrs={'type': 'date'}),
            'content': forms.Textarea(attrs={'placeholder': "What's on your mind today?", 'class': 'form-control textarea-form-content'}),
        }
