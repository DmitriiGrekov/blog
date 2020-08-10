from django.contrib.sitemaps import Sitemap  
from .models import QuestionsModel 
  
  
class QuestionsSiteMap(Sitemap):  
  
    def items(self):  
        return QuestionsModel.objects.all()  
