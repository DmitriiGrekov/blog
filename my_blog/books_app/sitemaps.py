from django.contrib.sitemaps import Sitemap  
from .models import Books
  
  
class BooksSiteMap(Sitemap):  
  
    def items(self):  
        return Books.objects.all()  
