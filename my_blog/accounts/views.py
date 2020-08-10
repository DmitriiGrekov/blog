from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from questions.models import QuestionsModel
from itertools import chain

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def register(request):
    if request.method == 'POST':
        user_form =RegisterForm(request.POST) 
        if user_form.is_valid():
            user_form.save()
            return redirect('login') 

        else:
           message = 'Такой email или Логин уже существует'
           return render(request,'register/register.html',{'form':user_form,'message':message})
    else:
        user_form = RegisterForm()
        return render(request,'register/register.html',{'form':user_form})

def my_questions(request):
    
    if request.user.is_authenticated:

        questions=request.user.questions.all()
        paginator = Paginator(questions,5)
        page = request.GET.get('page')
        try:
            questions= paginator.page(page)
        except PageNotAnInteger:
            questions= paginator.page(1)
        except EmptyPage:
            questions= paginator.page(paginator.num_pages)

        return render(request,'register/my_questions.html',{'questions':questions})

def favourite_articles(request):
    if request.user.is_authenticated:

        favourite_article=request.user.articles_like.all()
        favourite_service_article=request.user.service_like.all()
        favourite_articles= list(chain(favourite_article, favourite_service_article)) 
        paginator = Paginator(favourite_articles,1)
        page = request.GET.get('page')
        try:
            favourite_articles= paginator.page(page)
        except PageNotAnInteger:
            favourite_articles= paginator.page(1)
        except EmptyPage:
            favourite_articles= paginator.page(paginator.num_pages)


        return render(request,'register/favourite_articles.html',{'favourite_articles':favourite_articles})
def favourite_books(request):
    if request.user.is_authenticated:
        favourite_books = request.user.books_like.all()
        paginator = Paginator(favourite_books,1)
        page = request.GET.get('page')
        try:
            favourite_articles= paginator.page(page)
        except PageNotAnInteger:
            favourite_articles= paginator.page(1)
        except EmptyPage:
            favourite_articles= paginator.page(paginator.num_pages)


        return render(request,'register/favourite_books.html',{'favourite_articles':favourite_articles})
       


















