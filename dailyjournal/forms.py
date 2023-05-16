from django import forms
from .models import JournalLog


class JournalForm(forms.ModelForm):
    class Meta:
        model = JournalLog
        fields = ['created_on', 'content', 'daily_rating', 'featured_image']
        ordering = ['-created_on']
