from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'service'

urlpatterns = [
    path('service/<slug:slug>/',views.services,name='services'),
    path("<slug:slug>/<slug:ser>/",views.service_detail,name='service_post'),

    path('like/',views.service_like,name='service_like'),
]
