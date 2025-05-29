from django.db import models
from django.core.validators import FileExtensionValidator

class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    photo = models.ImageField(
        upload_to='photos/',
        validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])],
        verbose_name="Фото"
    )
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=20, verbose_name="Телефон", blank=True)
    resume = models.FileField(
        upload_to='resumes/',
        validators=[FileExtensionValidator(['pdf', 'doc', 'docx'])],
        verbose_name="Резюме",
        blank=True,
        null=True
    )
    
    class Meta:
        abstract = True

class Me(Person):
    vk_link = models.URLField(verbose_name="Ссылка VK", blank=True)
    telegram = models.CharField(max_length=50, verbose_name="Telegram", blank=True)
    
    def __str__(self):
        return f"Мой профиль: {self.name}"

class ProgramManager(Person):
    POSITION_CHOICES = [
        ('head', 'Академический руководитель'),
        ('manager', 'Менеджер программы'),
    ]
    position = models.CharField(
        max_length=20,
        choices=POSITION_CHOICES,
        verbose_name="Должность"
    )
    
    def __str__(self):
        return f"{self.get_position_display()}: {self.name}"

class Classmate(Person):
    year = models.PositiveSmallIntegerField(verbose_name="Год поступления")
    
    def __str__(self):
        return f"Сокурсник: {self.name}"

class EducationalProgram(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название программы")
    description = models.TextField(verbose_name="Описание")
    link = models.URLField(verbose_name="Ссылка на страницу ОП")
    what_will_i_learn = models.TextField(verbose_name="Что я буду изучать")
    advantages = models.TextField(verbose_name="Преимущества программы")
    prospects = models.TextField(verbose_name="Перспективы после обучения")
    
    def __str__(self):
        return self.name