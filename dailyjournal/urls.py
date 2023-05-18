from django.urls import path
from .views import LogJournalView, JournalListView

app_name = 'dailyjournal'

urlpatterns = [
    path('log/', LogJournalView.as_view(), name='log_journal'),
    path('journal/', JournalListView.as_view(), name='journal_list'),
]
