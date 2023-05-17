from django import forms
from django.forms import DateInput
from .models import JournalLog


class JournalForm(forms.ModelForm):
    class Meta:
        model = JournalLog
        fields = ['created_on', 'content', 'featured_image']
        ordering = ['-created_on']
        widgets = {
            'created_on': DateInput(attrs={'type': 'date'}),
            'content': forms.Textarea(attrs={'placeholder': "What's on your mind today?", 'class': 'form-control textarea-form-content'}),
        }
