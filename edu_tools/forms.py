from django import forms

from users.models import User


class UserForm(forms.Form):
    class meta:
        model = User
        fields = '__all__'
    