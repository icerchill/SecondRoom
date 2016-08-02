from django import forms
from .models import user

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = user
        fields = [
            'email',
            'alias',
            'password',
            'avatar',
            'cellNumber'
        ]