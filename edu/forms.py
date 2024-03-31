from django import forms
from .models import Lessons

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ['data', 'topic', 'additionals', 'home_work', 'email']
        widgets = {
            'data': forms.DateInput(attrs={'class': 'form-control'}),
            'topic': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'additionals': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'home_work': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }