from django.urls import path
from .views import LogJournalView, JournalListView, DeleteJournalEntryView

"""
Defines the URL patterns for all the journal-related features.
"""
app_name = 'dailyjournal'

urlpatterns = [
    path('log/', LogJournalView.as_view(), name='log_journal'),
    path('journal/', JournalListView.as_view(), name='journal_list'),
    path('delete/<int:pk>/', DeleteJournalEntryView.as_view(), name='delete_entry'),
]
