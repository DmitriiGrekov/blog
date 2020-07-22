from django.forms import ModelForm,TextInput,EmailInput,Textarea
from .models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']
        widgets = {'name':TextInput(attrs = {'class':'form-control','placeholder':'Имя'}),
                'email':EmailInput(attrs = {'class':'form-control','placeholder':'Email'}),
                'body':Textarea(attrs = {'class':'form-control mb-2','id':'exampleFormControlTextarea1','rows':'3','placeholder':'Текст комментария'})}


