from django.db import models
from django.urls import reverse

# Create your models here.


class Books(models.Model):
    title = models.CharField(max_length = 255)
    slug = models.SlugField()
    books_file = models.FileField(upload_to = 'books/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):

        return reverse('books_app:books_detail', args = [self.slug])
