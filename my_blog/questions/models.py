from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager
from django.urls import reverse
from pytils.translit import slugify
# Create your models here.

class QuestionsModel(models.Model):
    title = models.CharField(max_length = 250)
    name = models.CharField(max_length = 100,default='None',blank=True)
    email = models.EmailField()
    question = models.TextField(verbose_name = 'Вопрос')
    publish = models.DateTimeField(auto_now_add = True)
    answer = models.TextField(blank = True)
    slug = models.SlugField(unique = True)
    question_image = models.ImageField(upload_to='images/',blank = True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='questions')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ('-publish',)

    tags = TaggableManager(verbose_name='Тэгги')
    
    def get_absolute_url(self):
        return reverse('questions:question_details',args = [self.slug])
    def save(self,  *args, **kwargs):
        self.slug = slugify(self.title)
        print(self.slug)
        return super(QuestionsModel, self).save(*args, **kwargs)



class Comment(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    post = models.ForeignKey(QuestionsModel,on_delete = models.CASCADE,related_name = 'comments')
    active = models.BooleanField(default = True)

    class Meta:
        verbose_name = 'Комментарий к ответу'
        verbose_name_plural = 'Комментарии к ответу'

    def __str__(self):
        return self.name


