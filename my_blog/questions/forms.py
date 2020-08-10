from django.forms import ModelForm,TextInput,EmailInput,Textarea,FileInput
from .models import Comment,QuestionsModel

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
        widgets = {'name':TextInput(attrs = {'class':'form-control','placeholder':'Имя'}),
                'email':EmailInput(attrs = {'class':'form-control','placeholder':'Email'}),
                'body':Textarea(attrs = {'class':'form-control mb-2','id':'exampleFormControlTextarea1','rows':'3','placeholder':'Текст комментария'})}


class QuestionForm(ModelForm):
    class Meta:
        model = QuestionsModel
        fields = ['title','name','email','tags','question','question_image']
        widgets = {'title':TextInput(attrs={'class':'form-control mb-2 w-100','placeholder':'Заголовок'}),
                   'name':TextInput(attrs={'class':'form-control mb-2 w-100','placeholder':'Имя'}),
                   'email':EmailInput(attrs ={'class':'form-control mb-2 w-100','placeholder':'Email'}),
                   'tags':TextInput(attrs = {'class':'form-control mb-2 w-100','placeholder':'Ключевые слова (пример: html, css, js)'}),
                   'question':Textarea(attrs = {'class':'form-control mb-2 w-100','id':'exampleFormControlTextarea1','placeholder':'Текст вопроса'}),
                   'question_image':FileInput(attrs = {'class':'form-control-file mb-2 '})}
    

