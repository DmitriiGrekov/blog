from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def list_book(request):
    return HttpResponse('hello')


def book_detail(request,slug):
    return HttpResponse('hi')
