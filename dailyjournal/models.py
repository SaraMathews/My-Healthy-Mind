from django.db import models
from django import forms
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class JournalLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField()
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.content
