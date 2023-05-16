from django.views.generic import CreateView
from .models import JournalLog
from .forms import JournalForm


class LogJournalView(CreateView):
    model = JournalLog
    form_class = JournalForm
    template_name = 'daily_journal.html'
