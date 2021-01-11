from django.shortcuts import render
from django.utils import timezone
from .models import Post

def about(request):
    return render(request, 'withsite/about.html', {})

def contact(request):
    return render(request, 'withsite/contact.html', {})

def fashion(request):
    return render(request, 'withsite/fashion.html', {})

def index(request):
    return render(request, 'withsite/index.html', {})

def single(request):
    return render(request, 'withsite/single.html', {})

def travel(request):
    return render(request, 'withsite/travel.html', {})