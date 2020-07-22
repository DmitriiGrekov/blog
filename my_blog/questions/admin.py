from django.contrib import admin
from .models import QuestionsModel,Comment

@admin.register(QuestionsModel)
class QuestionsModelAdmin(admin.ModelAdmin):
    list_display = ("title",'name') 
    prepopulated_fields = {'slug':('title',)}
    list_filter = ('title','name')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter =  ('name',)
