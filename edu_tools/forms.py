from django import forms

from users.models import User

from edu.models import Lessons
from django.forms.widgets import DateInput

class UserForm(forms.Form):
    class Meta:
        model = User
        fields = '__all__'


class LessonsForm(forms.ModelForm):
    class Meta:
        model = Lessons
        fields = ['topic', 'additionals', 'home_work', 'data', 'email', 'is_done']
    
        
    topic = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    additionals = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    home_work = forms.CharField(label='Домашнее задание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    data = forms.DateField(label='Выберите дату', widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    is_done = forms.BooleanField(label='Не скрывать', required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))