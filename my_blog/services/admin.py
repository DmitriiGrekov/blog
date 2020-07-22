from django.contrib import admin
from .models import ServiceModel,ServicePost,Comment

# Register your models here.

@admin.register(ServiceModel)
class ServiceModelAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    prepopulated_fields = {'slug':('title',)}



@admin.register(ServicePost)
class ServicePostModelAdmin(admin.ModelAdmin):
    list_display = ('title','author','slug','publish')
    prepopulated_fields = {'slug':('title',)}

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    list_display = ('name','email')
