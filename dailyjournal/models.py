from django.db import models
from django import forms
from django.contrib.auth.models import User


class JournalLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField()
    content = models.TextField()

    def __str__(self):
        return self.content
