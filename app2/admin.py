from django.contrib import admin
from .models import Me, ProgramManager, Classmate, EducationalProgram


@admin.register(Me)
class MeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'vk_link', 'telegram')
    search_fields = ('name', 'email')
    readonly_fields = ('resume',)


@admin.register(ProgramManager)
class ProgramManagerAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'email', 'phone')
    list_filter = ('position',)
    search_fields = ('name', 'email')


@admin.register(Classmate)
class ClassmateAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'year')
    list_filter = ('year',)
    search_fields = ('name', 'email')


@admin.register(EducationalProgram)
class EducationalProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'link')
    search_fields = ('name',)
