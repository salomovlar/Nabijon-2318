from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'price', 'sold')
    list_filter = ('sold',)
    search_fields = ('name', 'author')
    ordering = ('name',)
