from django.urls import path
from .views import LogJournalView

app_name = 'dailyjournal'

urlpatterns = [
    path('log/', LogJournalView.as_view(), name='log_journal'),
]
