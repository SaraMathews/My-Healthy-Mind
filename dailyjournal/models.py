from django.db import models
from django import forms
from django.contrib.auth.models import User

"""
Describes a user's journal.
Includes fields for the owner of the journal, the date when the journal was 
created and the content. 
"""

class JournalLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.content
