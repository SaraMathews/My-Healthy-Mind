from django.shortcuts import render
from django.views.generic import TemplateView
from .models import DailyQuote
from random import choice

"""
Renders the home page template with a randomly selected quote from the database. 
If no quotes exists in the database, a default quote is shown instead. 
"""

class QuoteView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quotes = DailyQuote.objects.all()
        if quotes.exists():
            random_quote = choice(quotes)
            context['quote'] = random_quote
        else:
            context['quote'] = DailyQuote(
                quote="Before you marry a person, you should first make them use a computer with slow Internet to see who they really are", author="Will Ferrell")
        return context
