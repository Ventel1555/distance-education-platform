from django import forms
from django.contrib.auth.forms import AuthenticationForm


class AuthenticationForm(AuthenticationForm):
    """Custom Authentication form."""
    
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingInput',
                'placeholder': '123name321',
            },
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'floatingPassword',
                'placeholder': 'Qwerty123',
            },
        ),
    )
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'