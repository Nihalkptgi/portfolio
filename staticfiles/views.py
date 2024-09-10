from django.shortcuts import render
from django.contrib.staticfiles import finders

finders.find('css/style.css')


def home(request):
    return render(request, 'home.html')