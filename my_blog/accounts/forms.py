from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm,TextInput,EmailInput,Textarea,FileInput,PasswordInput
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length = 254,help_text = 'Введите Email',widget=EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    password1 = forms.CharField(help_text='Введите паролт',widget=PasswordInput(attrs={'class':'form-control','placeholder':'Пароль'}))
    
    password2 = forms.CharField(help_text='Введите паролт',widget=PasswordInput(attrs={'class':'form-control','placeholder':'Подтверждение пароля'}))
    firstname=forms.CharField(help_text='Введите Имя',widget=TextInput(attrs={'class':'form-control','placeholder':'Введите Имя'}))

    lastname=forms.CharField(help_text='Введите фамилию',widget=TextInput(attrs={'class':'form-control','placeholder':'Введите Фамилию'}))
    User._meta.get_field('email')._unique = True

    User._meta.get_field('username')._unique = True
    class Meta:
        model = User
        fields = ('username','email','password1','password2','first_name','last_name')
        widgets = {'username':TextInput(attrs = {'class':'form-control','placeholder':'Логин'})}

