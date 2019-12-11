from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'bubbleapp/homepage.html')

def bubblehtml(request):
    return render(request, 'bubbleapp/bubbleschedule.html')

# Create your views here.
