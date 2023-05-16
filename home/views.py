from django.shortcuts import render
from django.views import generic, View

# Create your views here.


def home(request):
    return render(request, 'base.html')


def home_page(request):
    return render(request, 'home_page.html')
