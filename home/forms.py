from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django import forms
from people.models import People

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30,
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))



class UserCreationForm(forms.ModelForm):

    class Meta:
        model = People
        fields = ("email","username","nickname","password")

        widgets = {
            'email': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your email', 'required': True, }),
            'username': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your username', 'required': True, }),
            'nickname': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your in-game nickname', 'required': True, }),
            'password': forms.PasswordInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter your password', 'required': True, }),
        }