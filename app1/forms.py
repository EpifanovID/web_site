from django import forms
from .models import MathProgramFeedback

from django import forms
from .models import MathProgramFeedback

class ProgramFeedbackForm(forms.ModelForm):
    # Варианты для выпадающего списка
    RECOMMEND_CHOICES = [
        (True, 'Да, рекомендую'),
        (False, 'Нет, не рекомендую'),
    ]
    
    recommend = forms.ChoiceField(
        choices=RECOMMEND_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'}),
        initial=True,
        label='Я рекомендую программу "Прикладная математика" другим'
    )
    
    class Meta:
        model = MathProgramFeedback
        fields = [
            'name', 'email', 'rating', 
            'curriculum_opinion', 'teaching_quality', 
            'improvements', 'recommend'
        ]
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 11)]),
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
            })
        }
        labels = {
            'rating': 'Оцените программу (1-10)'
        }