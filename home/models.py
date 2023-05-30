from django.db import models


class DailyQuote(models.Model):
    """
    Describes the Daily Quote
    Includes fields for the context of the quote, the author of the quote and the
    date it was created.
    """
    quote = models.TextField()
    author = models.CharField(max_length=255)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.quote

    class Meta:
        ordering = ['-date_created']
