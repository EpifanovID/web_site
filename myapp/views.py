from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def section1(request):
    return render(request, 'section1.html')

def section2(request):
    return render(request, 'section2.html')