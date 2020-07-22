from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'books_app'

urlpatterns = [
    path('', views.list_book,name='list_book'),
    path('<slug:slug>',views.book_detail,name='book_detail'),

]
