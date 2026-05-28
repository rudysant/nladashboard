# Register your models here.
from django.contrib import admin
from .models import Books

class BooksTitle(admin.ModelAdmin):
    list_display = ("book_title", "book_publisher",)

# Register your models here.
admin.site.register(Books, BooksTitle)