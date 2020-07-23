from django.contrib import admin
from .models import Books,Category
# Register your models here.

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    list_filter = ('title','slug')
    prepopulated_fields = {'slug':('title',)}
    ordering = ('title','-publish')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    prepopulated_fields = {'slug':('title',)} 



