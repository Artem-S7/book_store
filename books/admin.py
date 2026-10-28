from django.contrib import admin
from .models import Book, Category

class BookInline(admin.TabularInline):
    model = Book

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'author']
    list_filter = ['category']

class CategoryAdmin(admin.ModelAdmin):
    inlines = [BookInline]
    search_fields = ('name', 'slug')
    list_filter = ('name', 'slug')

admin.site.register(Book, BookAdmin)
admin.site.register(Category, CategoryAdmin)

