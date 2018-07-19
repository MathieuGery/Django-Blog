from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
     return render(request, 'about.html')