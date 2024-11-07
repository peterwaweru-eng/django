# from django.shortcuts import render
from django.shortcuts import render


# Create your views here.

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def home(request):
    return render(request,'home.html')

def base(request):
    return render(request,'base.html')

def contact(request):
    return render(request,'contact.html')
