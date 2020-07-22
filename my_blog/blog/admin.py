from django.contrib import admin
from .models import Article,Comment,Category

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','publish','status')
    list_filter = ('status','create','publish','author')
    search_fields = ('title','body')
    prepopulated_fields = {'slug':('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status','publish')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','date')
    list_filter = ('name','email')
    search_fields = ('name','email')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)} 
