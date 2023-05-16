from django.views.generic import CreateView
from django import forms
from .models import JournalLog
from .forms import JournalForm


class LogJournalView(CreateView):
    model = JournalLog
    form_class = JournalForm
    template_name = 'daily_journal.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.fields['content'].widget.attrs['placeholder'] = "What's on your mind today?"
        form.fields['content'].widget.attrs['class'] = "form-control textarea-form-content"
        return super().form_valid(form)
