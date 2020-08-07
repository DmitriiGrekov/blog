from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Books,Category
from services.models import ServiceModel
from .forms import CommentForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
# Create your views here.


def list_book(request):
    search_query = request.GET.get('search','')
    if search_query:
        books= Books.objects.filter(Q(title__icontains = search_query)| Q(description__icontains= search_query))
    else:
        books= Books.objects.all().order_by('-publish')
    category = Category.objects.all()[0:5]
    paginator = Paginator(books,1)
    page = request.GET.get('page')
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)




    return render(request,'books_app/books_list.html',{'books':books,'categories':category})

def book_detail(request,slug):


    book= get_object_or_404(Books,slug = slug) 
    categories = Category.objects.all()[0:5]

    comments = book.comments.filter(active = True)
    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.book= book 
            new_comment.save()



            

    form = CommentForm()


    return render(request,'books_app/book_detail.html',{'book':book,'comments':comments,'form':form,'categories':categories})




def download_book(request,slug):
    book = Books.objects.get(slug=slug)
    return redirect(book.books_file.url)


def category_book(request,slug):

    category = Category.objects.get(slug = slug)
    books = Books.objects.filter(category = category)
    categories = Category.objects.all()
    paginator = Paginator(books,1)
    page = request.GET.get('page')
    

    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)




    return render(request,'books_app/books_list.html',{"books":books,'categories':categories})









