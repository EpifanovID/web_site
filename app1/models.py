from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Об авторе
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='app1/static/app1/images/')

class ProgramSupervisor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(upload_to='app1/images/')

class ProgramManager(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(upload_to='app1/images/')

class ProgramInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    supervisor = models.OneToOneField(ProgramSupervisor, on_delete=models.CASCADE)
    manager = models.OneToOneField(ProgramManager, on_delete=models.CASCADE)

class Classmate(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='app1/images/')

# Фотрма

class MathProgramFeedback(models.Model):
    
    # Основная информация
    name = models.CharField('Имя', max_length=100, blank=True)
    email = models.EmailField('Email', blank=True)
    
    curriculum_opinion = models.TextField(
        'Ваше мнение о учебном плане',
        help_text='Соответствие современным требованиям, полнота курсов и т.д.'
    )
    
    teaching_quality = models.TextField(
        'Качество преподавания',
        help_text='Ваше впечатление от преподавательского состава',
        blank=True
    )

    rating = models.PositiveSmallIntegerField(
        'Оценка программы (1-10)',
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        null=True,
        blank=True,
        help_text='Оцените программу по шкале от 1 до 10, где 10 - отлично'
    )
    
    
    improvements = models.TextField(
        'Что можно улучшить?',
        help_text='Ваши предложения по улучшению программы',
        blank=True
    )
    
    recommend = models.BooleanField(
        'Рекомендовали бы вы эту программу?',
        default=True
    )
    
    created_at = models.DateTimeField('Дата отправки', auto_now_add=True)
    
    class Meta:
        verbose_name = 'Отзыв о программе'
        verbose_name_plural = 'Отзывы о программе'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Отзыв от {self.name or 'анонима'} ({self.created_at.strftime('%d.%m.%Y')})"