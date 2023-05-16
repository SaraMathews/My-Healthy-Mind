from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('home_page/', views.home_page, name='home_page'),
]
