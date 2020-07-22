from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib.sitemaps import Sitemap

class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name='Категория')
    slug = models.SlugField(blank = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def get_absolute_url(self):
        return reverse('blog:category_list', args = [self.slug])



class Article(models.Model):
    STATUS_CHOICE = (
            ('draft',"Draft"),
            ('publish',"Publish")
            )
    author = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'blog_posts')
    category = models.ForeignKey(Category,on_delete = models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length = 250,unique = True)
    body = models.TextField()
    publish = models.DateTimeField(default = timezone.now)
    create = models.DateTimeField(auto_now_add = True)
    update = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 10,choices = STATUS_CHOICE,default = 'draft')
    image = models.ImageField()

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:post_detail',  args = [self.publish.year,self.publish.month,self.publish.day,self.slug])

class Comment(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    post = models.ForeignKey(Article,on_delete = models.CASCADE,related_name = 'comments')
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.name

class BlogSiteMap(Sitemap):
    changefreq = 'never'
    priopiry = 0.5

    def items(self):
        return Article.objects.all()


