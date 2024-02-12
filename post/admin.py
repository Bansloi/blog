# admin.py
from django.contrib import admin
from.models import  Post
from .author import Author
from .category import Category



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'published', 'status')
    list_filter = ('published', 'status', )
    search_fields = ('title', )

admin.site.register(Author) 
admin.site.register(Category) 

admin.site.site_header = 'Bansloi Admin'
admin.site.site_title = 'Bansloi Blog Admin'
