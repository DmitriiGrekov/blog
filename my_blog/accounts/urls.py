from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'accounts'

urlpatterns = [
        path('register/',views.register,name='register'),
        path('my_questions/',views.my_questions,name='my_questions'),
        path('favourite_articles/',views.favourite_articles,name='favourite_articles'),
        path('favourite_books/',views.favourite_books,name='favourite_books'),
]
