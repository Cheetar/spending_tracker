from django.shortcuts import render


def home(request):
    render(request, 'tracker/home.html')


def contact(request):
    render(request, 'tracker/contect.html')
