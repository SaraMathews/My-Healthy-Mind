from django.shortcuts import render
from django.views.generic import TemplateView
from .models import DailyQuote


class QuoteView(TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        latest_quote = DailyQuote.objects.latest('date_created')
        context['quote'] = latest_quote
        return context
