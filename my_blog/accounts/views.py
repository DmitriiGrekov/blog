from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm

def register(request):
    if request.method == 'POST':
        user_form =RegisterForm(request.POST) 
        if user_form.is_valid():
            user_form.save()
            return redirect('login') 
    else:
        user_form = RegisterForm()
        return render(request,'register/register.html',{'form':user_form})
