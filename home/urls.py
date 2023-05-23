from django.urls import path
from .views import QuoteView

"""
Defines the URL pattern for the home-page related feature.
"""

app_name = 'home'


urlpatterns = [
    path('', QuoteView.as_view(), name='home'),
]
