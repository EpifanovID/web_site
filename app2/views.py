from django.shortcuts import render
from .models import Me, EducationalProgram, ProgramManager, Classmate

def home(request):
    return render(request, 'app2/home.html')

def about_me(request):
    my_profile = Me.objects.first()
    return render(request, 'app2/about_me.html', {'profile': my_profile})

def program(request):
    subjects = [
        "Математический анализ",
        "Линейная алгебра",
        "Дискретная математика",
        "Теория вероятностей",
        "Программирование на Python",
        "Анализ данных"
    ]
    return render(request, 'app2/program.html', {'subjects': subjects})

def management(request):
    managers = ProgramManager.objects.all()
    return render(request, 'app2/management.html', {'managers': managers})

def classmates(request):
    classmates_list = Classmate.objects.all()
    return render(request, 'app2/classmates.html', {'classmates': classmates_list})


