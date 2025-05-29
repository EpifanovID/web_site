from django.shortcuts import render, redirect
from .models import Author, ProgramInfo, Classmate
from .forms import ProgramFeedbackForm
from .models import MathProgramFeedback
from django.db.models import Avg, Count
from django.shortcuts import render

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
            return redirect('app1:feedback_thanks')
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

def feedback_list(request):
    # Получаем все отзывы, отсортированные по дате (новые сначала)
    feedbacks = MathProgramFeedback.objects.all().order_by('-created_at')
    
    return render(request, 'app1/feedback_list.html', {
        'feedbacks': feedbacks,
        'title': 'Таблица отзывов'
    })

def feedback_stats(request):
    # Основные метрики
    total_feedbacks = MathProgramFeedback.objects.count()
    avg_rating = MathProgramFeedback.objects.aggregate(Avg('rating'))['rating__avg'] or 0
    recommend_percent = MathProgramFeedback.objects.filter(recommend=True).count() / total_feedbacks * 100 if total_feedbacks > 0 else 0

    # Распределение оценок (простая версия)
    rating_counts = MathProgramFeedback.objects.values('rating').annotate(count=Count('id')).order_by('rating')

    return render(request, 'app1/feedback_stats.html', {
        'avg_rating': round(avg_rating, 2),
        'recommend_percent': round(recommend_percent, 1),
        'total_feedbacks': total_feedbacks,
        'rating_counts': rating_counts,
        'title': 'Статистика отзывов'
    })