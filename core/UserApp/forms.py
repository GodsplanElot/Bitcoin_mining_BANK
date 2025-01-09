from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'YourUsername',
        'class': 'form-control',
        'id': 'floatingInput',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'enter password',
        'class': 'form-control',
        'id': 'form-Password'
    }))

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'YourUsername',
        'class': 'form-control',
        'id': 'floatingInput',
    }))


    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'email',
        'class': 'form-control',
        'id': 'floatingInput',
    }))
    
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'enter password',
        'class': 'form-control',
        'id': 'form-Password'
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'reapet password',
        'class': 'form-control',
        'id': 'form-Password'
    }))