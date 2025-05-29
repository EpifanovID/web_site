from django.shortcuts import render, redirect
from .models import Author, ProgramInfo, Classmate
from .forms import ProgramFeedbackForm
from .models import MathProgramFeedback
from django.db.models import Avg, Count

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

from django.db.models import Case, When, Value, IntegerField

def feedback_list(request):
    # Получаем все отзывы
    feedbacks = MathProgramFeedback.objects.all()
    
    # Обработка параметров фильтрации
    rating_filter = request.GET.get('rating')
    recommend_filter = request.GET.get('recommend')
    search_query = request.GET.get('search')
    
    # Применяем фильтры
    if rating_filter and rating_filter != 'all':
        feedbacks = feedbacks.filter(rating=rating_filter)
    
    if recommend_filter and recommend_filter != 'all':
        feedbacks = feedbacks.filter(recommend=(recommend_filter == 'true'))
    
    if search_query:
        feedbacks = feedbacks.filter(
            Q(curriculum_opinion__icontains=search_query) |
            Q(teaching_quality__icontains=search_query) |
            Q(improvements__icontains=search_query) |
            Q(name__icontains=search_query)
        )
    
    # Обработка сортировки
    sort_by = request.GET.get('sort_by', '-created_at')
    valid_sort_fields = ['created_at', '-created_at', 'rating', '-rating', 'name', '-name']
    
    if sort_by in valid_sort_fields:
        # Специальная сортировка для рекомендаций
        if sort_by == 'recommend':
            feedbacks = feedbacks.annotate(
                recommend_order=Case(
                    When(recommend=True, then=Value(0)),
                    default=Value(1),
                    output_field=IntegerField()
                )
            ).order_by('recommend_order')
        else:
            feedbacks = feedbacks.order_by(sort_by)
    else:
        feedbacks = feedbacks.order_by('-created_at')  # сортировка по умолчанию
    
    return render(request, 'app1/feedback_list.html', {
        'feedbacks': feedbacks,
        'title': 'Таблица отзывов',
        'current_sort': sort_by,
        'rating_filter': rating_filter or 'all',
        'recommend_filter': recommend_filter or 'all',
        'search_query': search_query or '',
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