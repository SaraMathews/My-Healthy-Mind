from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'base.html')


def previous_journals(request):
    return render(request, 'previous_journals.html')


def daily_journal(request):
    return render(request, 'daily_journal.html')


def home_page(request):
    return render(request, 'home_page.html')
