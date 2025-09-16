
# Register your models here.
# blog/admin.py
from django.contrib import admin
from .models import Post, Category, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'publish', 'author', 'category')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)} # Auto-fill slug from title
    raw_id_fields = ('author',) # Make author selection easier for many users
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'approved')
    list_filter = ('approved', 'created_at')
    search_fields = ('author__username', 'content')