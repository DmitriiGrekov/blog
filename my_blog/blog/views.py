from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import Article,Category
from .forms import CommentForm
from django.db.models import Q
from services.models import ServiceModel
from services.models import ServicePost

def list(request):
    services = ServiceModel.objects.all()
    search_query = request.GET.get('search','')
    if search_query:
        articles = Article.objects.filter(Q(title__icontains = search_query)| Q(body__icontains = search_query))
    else:
        articles = Article.objects.all().filter(status='publish')
    categories = Category.objects.all()
    paginator = Paginator(articles,10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    return render(request,'blog/index.html',{"posts":posts,'page':page,'categories':categories,'services':services})





def post_detail(request,year,month,day,post):
    
    services = ServiceModel.objects.all()
    categoryes = Category.objects.all()
    post = get_object_or_404(Article,slug = post,status = 'publish',publish__year = year,publish__month = month,publish__day=day) 
    comments = post.comments.filter(active = True)

    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.post = post
            new_comment.save()



            

    form = CommentForm()
    return render(request,'blog/detail.html',{'post':post,'comments':comments,'form':form,'categories':categoryes,'services':services})

def post_category(request,slug):

    category = Category.objects.get(slug = slug)
    search_query = request.GET.get('search','')
    if search_query:
        posts= Article.objects.filter(Q(title__icontains = search_query)| Q(body__icontains = search_query))
    else:
        posts= Article.objects.filter(category = category)


    services = ServiceModel.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/category.html', {
        'category': category,
        'page': page,
        'posts': posts,
        'categories':categories,
        'services':services})
