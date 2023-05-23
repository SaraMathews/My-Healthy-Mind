from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

"""
Describes a user's journal.
Includes fields for the owner of the journal, the date when the journal was
created and the content.
"""


class JournalLog(models.Model):
    RATING_OPTIONS = (
        ('Amazing', 'Amazing'),
        ('Good', 'Good'),
        ('Okay', 'Okay'),
        ('Bad', 'Bad'),
        ('Awful', 'Awful'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField()
    content = models.TextField()
    rating = models.CharField(
        max_length=20, choices=RATING_OPTIONS, default='Okay')
    image = CloudinaryField(blank=True)

    def __str__(self):
        return self.content
