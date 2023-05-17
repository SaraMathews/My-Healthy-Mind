from django.views.generic import CreateView
from django.views.generic.list import ListView
from django import forms
from .models import JournalLog
from .forms import JournalForm
from django.urls import reverse_lazy


class LogJournalView(CreateView):
    model = JournalLog
    form_class = JournalForm
    template_name = 'daily_journal.html'
    success_url = reverse_lazy('dailyjournal:log_journal')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        print("Form data saved to the database.")
        return super().form_valid(form)
