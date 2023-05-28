from django.db import models

"""
Describes the Daily Quote
Includes fields for the context of the quote, the author of the quote and the
date it was created.
"""


class DailyQuote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.quote

    class Meta:
        ordering = ['-date_created']
