from django.shortcuts import render
from .models import Author, ProgramInfo, Classmate

def home(request):
    return render(request, 'app1/home.html')

def author(request):
    author_info = Author.objects.first()
    program_info = ProgramInfo.objects.select_related('supervisor', 'manager').first()
    classmates = Classmate.objects.all()

    return render(request, 'app1/author.html', {
        'author_info': author_info,
        'program_info': program_info,
        'classmates': classmates,
    })
