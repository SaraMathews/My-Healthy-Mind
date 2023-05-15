from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base.html')


def home_page(request):
    return render(request, 'home_page.html')


def daily_journal(request):
    return render(request, 'daily_journal.html')
