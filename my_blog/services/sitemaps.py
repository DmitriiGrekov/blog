from django.contrib.sitemaps import Sitemap  
from .models import ServicePost
  
  
class ServiceSiteMap(Sitemap):  
  
    def items(self):  
        return ServicePost.objects.all()
