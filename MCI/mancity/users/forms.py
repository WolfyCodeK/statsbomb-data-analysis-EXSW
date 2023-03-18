from django import forms
from .models import User

class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'type': 'password', 'class': 'form-control'}),
        }
