from services.models import ServiceModel
from blog.models import Article
def main(request):
    services =  ServiceModel.objects.all()
    if request.user.is_authenticated:

        user_question =request.user.questions.all()
        
        return {'services':services,'user_question':user_question}
    
    return {'services':services}


