from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'questions'

urlpatterns = [
    path('',views.show_questions,name='all_questions'),
    path('<slug:slug>',views.questions_detail, name='question_details'),
    path('tag/<slug:slug>',views.show_tag_questions,name ='tag_questions'),
    path('create_questions/',views.create_questions,name='create_questions'),
]


