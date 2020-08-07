from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm,TextInput,EmailInput,Textarea,FileInput,PasswordInput
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length = 254,help_text = 'Введите Email',widget=EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password1 = forms.CharField(help_text='Введите паролт',widget=PasswordInput(attrs={'class':'form-control','placeholder':'Пароль'}))
    
    password2 = forms.CharField(help_text='Введите паролт',widget=PasswordInput(attrs={'class':'form-control','placeholder':'Подтверждение пароля'}))
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        widgets = {'username':TextInput(attrs = {'class':'form-control','placeholder':'Логин'})}


