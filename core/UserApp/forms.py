from django import forms 
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name', 'middle_name', 'last_name',
            'address_one', 'address_two', 'country',
            'date_of_birth', 'mother_name', 'father_name',
        ]

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

    