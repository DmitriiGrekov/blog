from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50,verbose_name='Категория')
    slug = models.SlugField(blank = True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    def get_absolute_url(self):
        return reverse('books_app:category_book', args = [self.slug])



class Books(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    slug = models.SlugField()
    books_file = models.FileField(upload_to = 'books/')
    books_image = models.ImageField(upload_to = 'books/image/')
    publish = models.DateTimeField(auto_now_add = True)
    category = models.ForeignKey(Category,on_delete = models.CASCADE)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книгa'
        verbose_name_plural = 'Книги'

    def get_absolute_url(self):

        return reverse('books_app:book_detail', args = [self.slug])


class Comment(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    book= models.ForeignKey(Books,on_delete = models.CASCADE,related_name = 'comments')
    active = models.BooleanField(default = True)

    class Meta:
        ordering = ('-date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.name


