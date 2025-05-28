from django.shortcuts import render, redirect
from .models import Author, ProgramInfo, Classmate
from .forms import ProgramFeedbackForm
from .models import MathProgramFeedback

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

def feedback_form(request):
    print("Функция feedback_form вызвана")
    if request.method == 'POST':
        form = ProgramFeedbackForm(request.POST)
        if form.is_valid():
            print("Форма валидна, сохраняем...")
            form.save()
            print("Данные сохранены, перенаправляем...")
            return redirect('feedback_thanks')
        else:
            # Выводим ошибки валидации
            print("Ошибки валидации формы:", form.errors)
    else:
        form = ProgramFeedbackForm()
        print("GET-запрос, показываем пустую форму")
    
    return render(request, 'app1/feedback_form.html', {
        'form': form,
        'program_name': 'Прикладная математика'
    })

def feedback_thanks(request):
    return render(request, 'app1/feedback_thanks.html')