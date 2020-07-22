from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone


class ServiceModel(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.SlugField(blank = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-title',)
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def get_absolute_url(self):
        return reverse('service:services',  args = [self.slug])


class ServicePost(models.Model):
    STATUS_CHOICE = (
            ('draft',"Draft"),
            ('publish',"Publish")
            )
    author = models.ForeignKey(User,on_delete = models.CASCADE,related_name = 'service_post')

    service= models.ForeignKey(ServiceModel,on_delete = models.CASCADE)
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
        verbose_name = 'Статья сервиса'
        verbose_name_plural = 'Статьи сервиса'

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('service:service_post',  args = [self.service.slug,self.slug])


class Comment(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    post = models.ForeignKey(ServicePost,on_delete = models.CASCADE,related_name = 'comments')
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.name


