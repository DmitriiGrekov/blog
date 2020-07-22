from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import QuestionsModel,Comment
from services.models import ServiceModel
from .forms import CommentForm,QuestionForm
from taggit.models import Tag
from django.db.models import Q

# Create your views here.


def show_questions(request):
    all_questions = QuestionsModel.objects.all()
    services = ServiceModel.objects.all()
    tags = Tag.objects.all()[0:5]
    search_query = request.GET.get('search','')
    if search_query:
        all_questions= QuestionsModel.objects.filter(Q(title__icontains = search_query)| Q(question__icontains = search_query) | Q(tags__name__in=[search_query]))
    else:
        all_questions= QuestionsModel.objects.all()
    
    paginator = Paginator(all_questions,10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)



    return render(request,'questions/all_questions.html',{'posts':posts,'services':services,'tags':tags})



def questions_detail(request,slug):
    
    services = ServiceModel.objects.all()
     
     
    tags = Tag.objects.all()[0:5]

    question = get_object_or_404(QuestionsModel,slug = slug) 
    comments = question.comments.filter(active = True)
    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.post = question 
            new_comment.save()



            

    form = CommentForm()


    return render(request,'questions/question_detail.html',{'services':services,'question':question,'form':form,'comments':comments,'tags':tags})



def show_tag_questions(request,slug):
    all_questions = QuestionsModel.objects.all()
        
    tag = None
    if slug:
        tag = get_object_or_404(Tag,slug=slug)
        all_questions = all_questions.filter(tags__in=[tag])


    services = ServiceModel.objects.all()
    tags = Tag.objects.all()[0:5]

    paginator = Paginator(all_questions,10)
    page = request.GET.get('page')
    try:
        all_questions= paginator.page(page)
    except PageNotAnInteger:
        all_questions= paginator.page(1)
    except EmptyPage:
        all_questions= paginator.page(paginator.num_pages)



    return render(request,'questions/tag_questions.html',{'questions':all_questions,'services':services,'tags':tags,})


def create_questions(request):
    if request.method =='POST':
        form = QuestionForm(request.POST,request.FILES)
        if form.is_valid():
            new_question = form.save(commit = False)
            if QuestionsModel.objects.filter(title = new_question.title).exists():
                return render(request,'questions/create_question.html',{'form':form,'message':'Такой вопрос уже существует в базе'})
            
            new_question.save()
            for tag in form.cleaned_data['tags']:
                new_question.tags.add(tag)
            return redirect('questions:all_questions')



    form  = QuestionForm()
    return render(request,'questions/create_question.html',{'form':form})



