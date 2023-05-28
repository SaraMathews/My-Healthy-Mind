from django.contrib import admin
from .models import JournalLog

"""
Displays the list of journals, with user, when the journal was created and
the journal's content.
The admin can filter the journals by user and creation date.
"""


class AdminJournalLog(admin.ModelAdmin):
    list_display = ['user', 'created_on', 'content']
    list_filter = ['user', 'created_on']

    def get_queryset(self, request):
        queryset = super().get_queryset(request)

        if 'user__username' in request.GET:
            username = request.GET['user__username']
            queryset = queryset.filter(user__username=username)

        if 'created_on__date' in request.GET:
            date = request.GET['created_on__date']
            queryset = queryset.filter(created_on=date)

        return queryset


admin.site.register(JournalLog, AdminJournalLog)
