from django.shortcuts import render
from .models import Settings

def index(request):
    settings = Settings.objects.first()
    return render(request, 'index.html', {'settings': settings})

def contacts(request):
    settings = Settings.objects.first()
    return render(request, 'contacts.html', {'settings': settings})
