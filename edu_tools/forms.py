from django import forms

from users.models import User

from edu.models import Lessons, Subjects
from django.forms.widgets import DateInput

class UserForm(forms.Form):
    class Meta:
        model = User
        fields = '__all__'


class LessonsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(LessonsForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['class_field'].queryset = self.user.subjects_id.all()
            
    class Meta:
        model = Lessons
        fields = ['topic', 'additionals', 'home_work', 'data', 'email']

    class_field = forms.ModelChoiceField(queryset=Subjects.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    topic = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class': 'form-control'}))
    additionals = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    home_work = forms.CharField(label='Домашнее задание', widget=forms.Textarea(attrs={'class': 'form-control'}))
    data = forms.DateField(label='Выберите дату', widget=DateInput(attrs={'class': 'form-control', 'type': 'date'}))