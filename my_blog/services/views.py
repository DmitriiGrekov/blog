from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from .models import ServicePost,ServiceModel
from .forms import CommentForm
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


# Create your views here.

def services(request,slug):
    services = ServiceModel.objects.all()
    service= ServiceModel.objects.get(slug = slug)
    articles = ServicePost.objects.all().filter(service=service,status = 'publish')
    draft_articles = ServicePost.objects.all().filter(status ='draft' )
    paginator = Paginator(articles,1)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)


    
    
    return render(request,'services/services_list.html',{'posts':posts,'all_service':services,'page':page,'draft_articles':draft_articles,'service':service})

def service_detail(request,slug,ser):
    service = ServiceModel.objects.get(slug=slug)
    
    services = ServiceModel.objects.all()
    post = get_object_or_404(ServicePost,service = service ,slug = ser) 
    

    comments = post.comments.filter(active = True)

    if request.method == "POST":
        form  = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit = False)
            new_comment.post = post
            new_comment.save()



            

    form = CommentForm()
    return render(request,'services/services_post.html',{'post':post,'comments':comments,'form':form,'all_service':services})


    
@login_required
@require_POST
def service_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        try:
            post = ServicePost.objects.get(id=post_id)
            if action == 'like':
                post.service_like.add(request.user)
            else:
                post.service_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ok'})
