from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


DAILY_RATING_OPTIONS = (
    (1, 'Terrible'),
    (2, 'Bad'),
    (3, 'Okay'),
    (4, 'Good'),
    (5, 'Amazing'),
)


class JournalLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField()
    content = models.TextField()
    daily_rating = models.CharField(
        max_length=1, choices=DAILY_RATING_OPTIONS, default='3')
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.content
