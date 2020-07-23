from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Books,Category
from services.models import ServiceModel
from .forms import CommentForm
from django.shortcuts import redirect
# Create your views here.


def list_book(request):
    books = Books.objects.all().order_by('-publish')
    category = Category.objects.all()[0:5]


    services = ServiceModel.objects.all()
    return render(request,'books_app/books_list.html',{'books':books,'services':services,'categories':category})

def book_detail(request,slug):


    book= get_object_or_404(Books,slug = slug) 
    categories = Category.objects.all()[0:5]

    comments = book.comments.filter(active = True)
    services = ServiceModel.objects.all()
    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.book= book 
            new_comment.save()



            

    form = CommentForm()


    return render(request,'books_app/book_detail.html',{'book':book,'comments':comments,'services':services,'form':form,'categories':categories})




def download_book(request,slug):
    book = Books.objects.get(slug=slug)
    return redirect(book.books_file.url)


def category_book(request,slug):

    category = Category.objects.get(slug = slug)
    books = Books.objects.filter(category = category)

    return render(request,'books_app/books_list.html',{"books":books})









