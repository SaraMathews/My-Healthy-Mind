from django.contrib import admin
from .models import DailyQuote


"""
Registers the DailyQuote model with the Django admin site.
"""
admin.site.register(DailyQuote)