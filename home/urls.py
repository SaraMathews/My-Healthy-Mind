from django.urls import path
from .views import QuoteView


app_name = 'home'


urlpatterns = [
    path('', QuoteView.as_view(), name='home'),

]
