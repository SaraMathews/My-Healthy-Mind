from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('daily_journal/', views.daily_journal, name='daily_journal'),
    path('home_page/', views.home_page, name='home_page'),
]