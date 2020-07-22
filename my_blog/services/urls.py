from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'service'

urlpatterns = [
    path('<slug:slug>/',views.services,name='services'),
    path("<slug:slug>/<slug:ser>/",views.service_list,name='service_post'),
]
