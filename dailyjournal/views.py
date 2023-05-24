from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views import View
from django import forms
from .models import JournalLog
from .forms import JournalForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.mixins import (
    UserPassesTestMixin, LoginRequiredMixin
)


"""
View for logging a Daily Journal.
Allows the user to create a new journal entry.
"""


class LogJournalView(CreateView):
    model = JournalLog
    form_class = JournalForm
    template_name = 'daily_journal.html'
    success_url = reverse_lazy('dailyjournal:log_journal')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.image = self.request.FILES.get('image')
        messages.add_message(
            self.request,
            messages.SUCCESS,
            "Your Daily Journal has been submitted."
        )
        return super().form_valid(form)


"""
View for displaying a list of past journals
Displays a list of past journals for the logged in user.
"""


class JournalListView(ListView):
    model = JournalLog
    template_name = 'previous_journals.html'
    context_object_name = 'journal_entries'
    ordering = ['-created_on']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


"""
View for deleting a journal
Allows the user to delete their own journals.
"""


class DeleteJournalEntryView(
    LoginRequiredMixin, UserPassesTestMixin, DeleteView
):
    model = JournalLog
    success_url = reverse_lazy('dailyjournal:journal_list')
    template_name = 'journallog_confirm_delete.html'

    # Checks if the user passes the test to delete the journal
    def test_func(self):
        return self.request.user == self.get_object().user

    # Returns the context data that's used in the template rendering
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        entry = self.get_object()
        context['entry'] = entry
        return context

    # Deletes the journal and displays a success message
    def delete(self, request, *args, **kwargs):
        entry = self.get_object()
        response = super().delete(request, *args, **kwargs)
        formatted_date = entry.created_on.strftime("%B %d, %Y")
        messages.success(
            request, f"Your Journal for {formatted_date} has been deleted.")
        return response


"""
View for editing a journal
Allows the user to edit their own journals.
"""


class EditJournalEntryView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = JournalLog
    form_class = JournalForm
    template_name = 'edit_journal.html'
    success_url = reverse_lazy('dailyjournal:journal_list')

    # Checks if the user passes the test to edit the journal
    def test_func(self):
        return self.request.user == self.get_object().user

    # Gets the journal entry based on the given entry_id
    def get_object(self, queryset=None):
        entry_id = self.kwargs.get('entry_id')
        return get_object_or_404(JournalLog, id=entry_id)

    def form_valid(self, form):
        formatted_date = self.object.created_on.strftime("%B %d, %Y")
        messages.success(
            self.request, f"Your Journal for {formatted_date} has been updated.")
        return super().form_valid(form)
