from django.contrib import admin
from .models import Author, ProgramSupervisor, ProgramManager, ProgramInfo, Classmate, MathProgramFeedback

# Регистрируем существующие модели
admin.site.register(Author)
admin.site.register(ProgramSupervisor)
admin.site.register(ProgramManager)
admin.site.register(ProgramInfo)
admin.site.register(Classmate)

# Регистрируем новую модель MathProgramFeedback
@admin.register(MathProgramFeedback)
class MathProgramFeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'rating', 'created_at', 'recommend')  # Добавили rating
    list_filter = ('recommend', 'rating', 'created_at')  # Добавили rating
    search_fields = ('name', 'email', 'curriculum_opinion')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ("Контактная информация", {
            "fields": ("name", "email"),
            "description": "Основные данные отправителя"
        }),
        ("Оценка программы", {
            "fields": ("rating",),
        }),
        ("Содержание отзыва", {
            "fields": ("curriculum_opinion", "teaching_quality", "improvements"),
            "classes": ("collapse",)
        }),
        ("Рекомендация", {
            "fields": ("recommend", "created_at")
        }),
    )