from django.shortcuts import render


def home(request):
    return render(request, 'tracker/home.html')


def about(request):
    return render(request, 'tracker/about.html')
