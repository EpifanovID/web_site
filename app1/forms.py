from django import forms
from .models import MathProgramFeedback

class ProgramFeedbackForm(forms.ModelForm):
    class Meta:
        model = MathProgramFeedback
        fields = [
            'name', 'email', 
            'curriculum_opinion', 'teaching_quality',
            'improvements', 'recommend'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваше имя (необязательно)'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ваш email (необязательно)'
            }),
            'curriculum_opinion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Что вы думаете о учебном плане?'
            }),
            'teaching_quality': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ваше мнение о качестве преподавания'
            }),
            'improvements': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ваши предложения по улучшению'
            }),
            'recommend': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'recommend': 'Я рекомендую программу "Прикладная математика" другим'
        }